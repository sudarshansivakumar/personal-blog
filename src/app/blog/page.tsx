import Link from 'next/link';
import { getAllPosts } from '@/lib/blog';
import { formatDate } from '@/lib/utils'; // Assuming you have this utility

export default function BlogListPage() {
  const posts = getAllPosts();

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <header className="flex justify-start mb-8">
        <nav className="flex space-x-6">
          <Link href="/" className="text-lg font-semibold hover:underline">
            Home
          </Link>
          <Link href="/blog" className="text-lg font-semibold hover:underline">
            Blog
          </Link>
        </nav>
      </header>

      <main>
        <h1 className="text-4xl font-bold mb-8">Blog Posts</h1>

        {posts.length === 0 ? (
          <p className="text-lg mb-12">No blog posts found. Check back soon!</p>
        ) : (
          <div className="grid gap-8">
            {posts.map((post) => (
              <article key={post.slug} className="p-6 border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200">
                <h2 className="text-2xl font-semibold mb-2">
                  <Link href={`/blog/${post.slug}`} className="hover:text-blue-700">
                    {post.title}
                  </Link>
                </h2>
                <div className="text-sm text-gray-500 mb-3">
                  {formatDate(post.date)}
                </div>
                <p className="text-gray-600 mb-4">{post.description}</p>
                <Link href={`/blog/${post.slug}`} className="text-blue-600 hover:underline font-medium">
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