import Link from 'next/link';
import { getAllPosts } from '@/lib/blog';
import { formatDate } from '@/lib/utils'; // Assuming you have this utility
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: "Word salad",
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
    <div className="max-w-2xl mx-auto px-6 py-12">
      <main>
        <h2 className="mb-8 mt-0">Posts</h2>

        {posts.length === 0 ? (
          <p className="text-lg mb-12">I promise there will be some writing here <s>soon</s> eventually.</p>
        ) : (
          <div className="space-y-8 pt-4">
            {posts.map((post) => (
              <article key={post.slug} className="group pb-6">
                <div className="flex justify-between items-baseline mb-3">
                  <h3 className="text-xl font-normal">
                    <Link 
                      href={`/blog/${post.slug}`}
                      className="hover:text-black transition-colors"
                    >
                      {post.title}
                    </Link>
                  </h3>
                  <span className="text-sm text-gray-400 opacity-0 group-hover:opacity-100 transition-opacity">
                    {formatDate(post.date)}
                  </span>
                </div>
                
                {post.description && (
                  <p className="text-gray-600 leading-relaxed text-sm">
                    {post.description}
                  </p>
                )}
              </article>
            ))}
          </div>
        )}
      </main>
    </div>
  );
} 