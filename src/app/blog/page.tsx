import Link from 'next/link';
import { getAllPosts } from '@/lib/blog';
import { formatDate } from '@/lib/utils'; // Assuming you have this utility
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: "Blog | Sudarshan's Blog",
  description: "Browse all blog posts by Sudarshan",
  icons: {
    icon: [
      { url: '/icon.png', type: 'image/png' },
      { url: '/icon.png', type: 'image/x-icon' }
    ],
  },
};

export default function BlogListPage() {
  const posts = getAllPosts();

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <main>
        <h1 className="text-4xl font-bold mb-8 mt-0">Blog Posts</h1>

        {posts.length === 0 ? (
          <p className="text-lg mb-12">No blog posts found. Check back soon!</p>
        ) : (
          <div className="grid gap-8">
            {posts.map((post) => (
              <article key={post.slug} className="p-6 border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200">
                <h2 className="text-2xl font-semibold mb-2 mt-0">
                  <Link href={`/blog/${post.slug}`}>
                    {post.title}
                  </Link>
                </h2>
                <div className="text-sm text-gray-500 mb-3">
                  {formatDate(post.date)}
                </div>
                <p className="text-gray-600 mb-4">{post.description}</p>
                <Link href={`/blog/${post.slug}`} className="font-medium">
                  Read more →
                </Link>
              </article>
            ))}
          </div>
        )}
      </main>
    </div>
  );
} 