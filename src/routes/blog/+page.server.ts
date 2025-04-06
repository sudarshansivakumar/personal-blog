import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

// Define an interface for the expected structure of post metadata
interface PostMetadata {
    slug: string;
    title: string;
    date: string; 
    description: string;
    tags: string[];
}

// Type definition for the page load function
/** @type {import('./$types').PageServerLoad} */
export async function load() {
    const postsDir = path.join(process.cwd(), 'src/content', 'posts');
    const allFilenames = fs.readdirSync(postsDir);

    // Filter out the template file by its name
    const filenames = allFilenames.filter(filename => filename !== 'template.md');

    // console.log('Found files (excluding template):', filenames);

    const posts: PostMetadata[] = filenames
        .filter((filename: string) => filename.endsWith('.md')) // Ensure we only process markdown files
        .map((filename: string) => {
            // console.log(`\nProcessing: ${filename}`); // Removed log
            const filePath = path.join(postsDir, filename);
            const fileContents = fs.readFileSync(filePath, 'utf8');
            try {
                const { data }: { data: any } = matter(fileContents); 
                // console.log(`Parsed data for ${filename}:`, JSON.stringify(data, null, 2)); // Removed log

                // Basic validation/defaults
                if (!data.slug) {
                    console.warn(`Post ${filename} is missing a slug. Skipping.`);
                    return null; // Return null for filtering later
                }
                if (!data.date) {
                    console.warn(`Post ${filename} is missing a date. Using default.`);
                    data.date = '1970-01-01'; // Default date if missing
                }

                // Construct the PostMetadata object
                const postData: PostMetadata = {
                    slug: data.slug,
                    title: data.title || 'Untitled Post',
                    date: data.date, 
                    description: data.description || '',
                    tags: Array.isArray(data.tags) ? data.tags : [] // Ensure tags is an array
                };
                return postData;
            } catch (parseError) {
                console.error(`Error parsing frontmatter for ${filename}:`, parseError);
                return null; // Skip files with parsing errors
            }
        })
        .filter((post): post is PostMetadata => post !== null); // Type predicate to filter out nulls and assert type

    // Sort posts by date, newest first
    posts.sort((a: PostMetadata, b: PostMetadata) => new Date(b.date).getTime() - new Date(a.date).getTime());

    return {
        posts: posts
    };
} 