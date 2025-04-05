import matter from 'gray-matter';
// Remove potentially problematic type import
// import type { PageLoad } from './$types'; 

// Enable prerendering for this page
export const prerender = true;

// Define an interface for the expected structure of post metadata
interface PostMetadata {
    slug: string;
    title: string;
    date: string;
    description: string;
    tags: string[];
    // Add path if needed later, but not strictly required for list view
    // path: string; 
}

// Remove explicit type annotation for load function
export const load = async () => {
    // Use import.meta.glob to find all markdown files at build time
    // Update glob options according to deprecation warning
    const modules = import.meta.glob('/content/posts/*.md', { eager: true, query: '?raw', import: 'default' });

    const posts: PostMetadata[] = Object.entries(modules)
        .map(([filepath, rawContent]) => {
            try {
                // Extract slug from filepath (e.g., /content/posts/my-slug.md -> my-slug)
                const slug = filepath.split('/').pop()?.replace('.md', '');
                
                if (!slug || slug === 'template') { // Skip if no slug or if it's the template
                    return null;
                }

                // Cast rawContent to string before passing to matter
                const { data }: { data: any } = matter(rawContent as string);

                if (!data.slug) {
                     console.warn(`Post at ${filepath} might have an incorrect slug in frontmatter, using filename-derived slug: ${slug}`);
                     data.slug = slug; // Use filename slug if frontmatter slug missing
                 }
                 if (data.slug !== slug) {
                    console.warn(`Frontmatter slug "${data.slug}" differs from filename-derived slug "${slug}" for ${filepath}. Using frontmatter slug.`);
                    // We'll still use the frontmatter slug primarily, but log warning
                 }

                if (!data.date) {
                    console.warn(`Post ${slug} is missing a date. Using default.`);
                    data.date = '1970-01-01';
                }

                const postData: PostMetadata = {
                    slug: data.slug, // Prioritize frontmatter slug
                    title: data.title || 'Untitled Post',
                    date: data.date,
                    description: data.description || '',
                    tags: Array.isArray(data.tags) ? data.tags : []
                };
                return postData;
            } catch (parseError) {
                console.error(`Error parsing frontmatter for ${filepath}:`, parseError);
                return null;
            }
        })
        .filter((post): post is PostMetadata => post !== null);

    // Sort posts by date, newest first
    posts.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

    return {
        posts: posts
    };
}; 