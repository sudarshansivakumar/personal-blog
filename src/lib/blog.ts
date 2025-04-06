import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

// Define the directory where blog posts are stored
const postsDirectory = path.join(process.cwd(), 'blogs');

export interface BlogPostData {
  slug: string;
  title: string;
  date: string;
  description: string;
  tags: string[];
}

export interface BlogPost extends BlogPostData {
  content: string;
}

/**
 * Reads all markdown files in the posts directory (excluding template.md)
 * and returns their slugs for generating static paths.
 */
export function getAllPostSlugs() {
  try {
    const fileNames = fs.readdirSync(postsDirectory);
    // Filter out non-markdown files and the template file
    return fileNames
      .filter(fileName => fileName.endsWith('.md') && fileName !== 'template.md')
      .map(fileName => ({
        params: {
          slug: fileName.replace(/\.md$/, ''),
        },
      }));
  } catch (error) {
    console.error('Error reading blog directory:', error);
    return [];
  }
}

/**
 * Reads all markdown files, parses their frontmatter, and returns
 * an array of blog post data objects, sorted by date (newest first).
 */
export function getAllPosts(): BlogPostData[] {
  try {
    const fileNames = fs.readdirSync(postsDirectory);
    const allPostsData = fileNames
      .filter(fileName => fileName.endsWith('.md') && fileName !== 'template.md')
      .map(fileName => {
        // Remove ".md" from file name to get slug
        const slug = fileName.replace(/\.md$/, '');
        // Read markdown file as string
        const fullPath = path.join(postsDirectory, fileName);
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        // Use gray-matter to parse the post metadata section
        const matterResult = matter(fileContents);
        // Combine the data with the slug
        return {
          slug,
          title: matterResult.data.title ?? 'Untitled Post',
          date: matterResult.data.date ? new Date(matterResult.data.date).toISOString() : new Date().toISOString(),
          description: matterResult.data.description ?? '',
          tags: matterResult.data.tags ?? [],
        };
      });

    // Sort posts by date
    return allPostsData.sort((a, b) => (a.date < b.date ? 1 : -1));

  } catch (error) {
    console.error('Error reading posts data:', error);
    return [];
  }
}

/**
 * Reads a specific blog post file by slug, parses frontmatter and content.
 * Returns the full blog post object including content.
 */
export function getPostBySlug(slug: string): BlogPost | null {
  const fullPath = path.join(postsDirectory, `${slug}.md`);
  try {
    const fileContents = fs.readFileSync(fullPath, 'utf8');
    // Use gray-matter to parse the post metadata section
    const matterResult = matter(fileContents);

    // Combine the data with the slug and content
    return {
      slug,
      title: matterResult.data.title ?? 'Untitled Post',
      date: matterResult.data.date ? new Date(matterResult.data.date).toISOString() : new Date().toISOString(),
      description: matterResult.data.description ?? '',
      tags: matterResult.data.tags ?? [],
      content: matterResult.content,
    };
  } catch (error) {
    // If the file doesn't exist or there's an error reading it
    console.error(`Error reading post ${slug}:`, error);
    return null;
  }
} 