import matter from 'gray-matter';
import { marked } from 'marked';
import { error } from '@sveltejs/kit';
// Remove separate type import
// import type { PageLoadEvent } from './$types';

// Enable prerendering for this page (and all slug pages)
export const prerender = true;

// Type definition (content will now be HTML string)
interface BlogPost {
    slug: string;
    title: string;
    date: string;
    description: string;
    tags: string[];
    content: string; // HTML content
}

// Remove explicit type annotation, add type for params
export const load = async ({ params }: { params: { slug: string } }) => {
    const { slug } = params;

    // Explicitly prevent loading the template slug
    if (slug === 'template') {
        error(404, 'Not found');
    }

    try {
        // Use import.meta.glob to find the specific file
        // Note: Vite requires the glob pattern to be somewhat static
        const modules = import.meta.glob('/content/posts/*.md', { as: 'raw' });
        const filePath = `/content/posts/${slug}.md`;
        
        // Check if the specific file path exists in the glob results
        if (!modules[filePath]) {
             error(404, `Post not found: ${slug}`);
        }

        // Load the raw content using the dynamic path from the glob results
        const moduleLoader = modules[filePath];
        if (!moduleLoader) { // Double check loader exists
            error(404, `Post loader not found: ${slug}`);
        }
        const rawContent = await moduleLoader() as string; // Load and cast to string

        const { data, content } = matter(rawContent);
        const htmlContent = await marked.parse(content);

        const postData: BlogPost = {
            slug: slug,
            title: data.title || 'Untitled Post',
            date: data.date || '1970-01-01',
            description: data.description || '',
            tags: Array.isArray(data.tags) ? data.tags : [],
            content: htmlContent
        };

        return {
            post: postData
        };
    } catch (err) {
        console.error(`Error loading post ${slug}:`, err);
        error(500, `Could not load post: ${slug}`);
    }
};
