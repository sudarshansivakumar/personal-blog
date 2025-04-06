import path from 'path';
import matter from 'gray-matter';
import type { PageServerLoad } from './$types';

// Define an interface for the expected structure of post metadata
interface PostMetadata {
	slug: string;
	title: string;
	date: string;
	description: string;
	tags: string[];
}

// Type definition for the page load function
export const load: PageServerLoad = async () => {
	// Use import.meta.glob to find all .md files in src/content/posts
	// The { query: '?raw', import: 'default', eager: true } options import the raw content eagerly
	// Note: The path is relative to the project root (where vite.config.ts is)
	const modules = import.meta.glob('/src/content/posts/*.md', { query: '?raw', import: 'default', eager: true });

	const posts: PostMetadata[] = Object.entries(modules)
		.map(([filePath, fileContents]) => {
			// Extract filename and slug from the filePath
			const filename = path.basename(filePath);
			// Skip the template file
			if (filename === 'template.md') {
				return null;
			}
			const slug = filename.replace('.md', ''); // Simple slug generation

			try {
				// Assert fileContents is a string before passing to matter
				const { data }: { data: any } = matter(fileContents as string);

				// Basic validation/defaults
				if (!data.slug) { // Check if frontmatter has slug, otherwise use filename-based slug
					data.slug = slug;
				} else if (data.slug !== slug) {
					console.warn(
						`Post ${filename} slug mismatch: frontmatter ('${data.slug}') vs filename ('${slug}'). Using filename.`
					);
					data.slug = slug; // Prioritize filename slug for consistency
				}

				if (!data.date) {
					console.warn(`Post ${filename} is missing a date. Using default.`);
					data.date = '1970-01-01'; // Default date if missing
				}

				// Construct the PostMetadata object
				const postData: PostMetadata = {
					slug: data.slug, // Use the determined slug
					title: data.title || 'Untitled Post',
					date: data.date,
					description: data.description || '',
					tags: Array.isArray(data.tags) ? data.tags : []
				};
				return postData;
			} catch (parseError) {
				console.error(`Error parsing frontmatter for ${filename}:`, parseError);
				return null; // Skip files with parsing errors
			}
		})
		.filter((post): post is PostMetadata => post !== null); // Filter out nulls (template or errors)

	// Sort posts by date, newest first
	posts.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

	return {
		posts: posts
	};
}; 