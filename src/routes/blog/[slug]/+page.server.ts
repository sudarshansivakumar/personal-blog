import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';
import { error } from '@sveltejs/kit';
import type { PageServerLoadEvent } from './$types';

// Type definition (content will now be HTML string)
interface BlogPost {
    slug: string;
    title: string;
    date: string;
    description: string;
    tags: string[];
    content: string; // Changed back to content (HTML string)
}

export async function load({ params }: PageServerLoadEvent) {
    const { slug } = params;

    // Explicitly prevent loading the template slug
    if (slug === 'template') {
        error(404, 'Not found'); // Treat template as not found
    }

    const postsDir = path.join(process.cwd(), 'content', 'posts');
    const filePath = path.join(postsDir, `${slug}.md`);

    if (!fs.existsSync(filePath)) {
        error(404, 'Post not found');
    }

    try {
        const fileContents = fs.readFileSync(filePath, 'utf8');
        const { data, content: rawContent } = matter(fileContents); 

        // Re-enable HTML conversion
        const htmlContent = await marked.parse(rawContent);

        const postData: BlogPost = {
            slug: slug,
            title: data.title || 'Untitled Post',
            date: data.date || '1970-01-01',
            description: data.description || '',
            tags: Array.isArray(data.tags) ? data.tags : [],
            // Pass HTML content
            content: htmlContent 
        };

        return {
            post: postData
        };
    } catch (err) {
        console.error(`Error loading post ${slug}:`, err);
        error(500, 'Could not load post');
    }
}

// Add this function to generate entries for prerendering
export async function entries() {
    const postsDir = path.join(process.cwd(), 'content', 'posts');
    try {
        const allFilenames = fs.readdirSync(postsDir);
        // Filter for markdown files, exclude template, and map to slug objects
        const slugs = allFilenames
            .filter(filename => filename.endsWith('.md') && filename !== 'template.md')
            .map(filename => ({ slug: filename.replace(/\.md$/, '') })); 
        return slugs;
    } catch (error) {
        // Log error and return empty array if directory read fails
        console.error("Error reading posts directory for prerendering entries:", error);
        return []; 
    }
}
