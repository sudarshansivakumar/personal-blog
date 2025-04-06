import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';
import { error } from '@sveltejs/kit';
import type { PageServerLoad, EntryGenerator } from './$types';

// --- Load all posts eagerly at build time ---
const modules = import.meta.glob('/src/content/posts/*.md', { query: '?raw', import: 'default', eager: true });

// Prepare a map for easy lookup: slug -> raw content
const postsContent: Record<string, string> = {};
for (const filePath in modules) {
	const filename = path.basename(filePath);
	if (filename === 'template.md') continue; // Skip template
	const slug = filename.replace('.md', '');
	postsContent[slug] = modules[filePath] as string; // Assert as string
}
// --- End build-time loading ---

// Type definition for a full blog post
interface BlogPost {
	slug: string;
	title: string;
	date: string;
	description: string;
	tags: string[];
	content: string; // HTML content
}

export const load: PageServerLoad = async ({ params }) => {
	const { slug } = params;

	// Explicitly prevent loading the template slug
	if (slug === 'template') {
		throw error(404, 'Not found');
	}

	// Find the content from the pre-loaded map
	const fileContents = postsContent[slug];

	if (!fileContents) {
		// If the slug doesn't exist in our map, it's a 404
		console.warn(`Post with slug '${slug}' not found in pre-loaded content.`);
		throw error(404, 'Post not found');
	}

	try {
		const { data, content: rawContent } = matter(fileContents); // No need for assertion here, already string

		// Convert markdown content to HTML
		const htmlContent = await marked.parse(rawContent);

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
	} catch (err: any) {
		// Errors here are likely parsing errors (matter, marked)
		console.error(`Error processing post ${slug}:`, err);
		throw error(500, 'Could not process post content');
	}
};

// Prerendering: Generate slugs from available files
export const entries: EntryGenerator = async () => {
	// Use import.meta.glob to find all .md files (only keys needed here)
	const modules = import.meta.glob('/src/content/posts/*.md');

	const slugs = Object.keys(modules).map((filePath) => {
		const filename = path.basename(filePath);
		// Exclude the template file from prerendering
		if (filename === 'template.md') {
			return null;
		}
		return { slug: filename.replace('.md', '') };
	});

	return slugs.filter((entry): entry is { slug: string } => entry !== null);
};
