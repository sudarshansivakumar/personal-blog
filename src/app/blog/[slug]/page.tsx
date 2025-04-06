import { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getAllPostSlugs, getPostBySlug } from '@/lib/blog';
import { formatDate } from '@/lib/utils';
import { MDXRemote } from 'next-mdx-remote/rsc';

interface Params {
  params: {
    slug: string;
  };
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const post = getPostBySlug(params.slug);
  
  if (!post) {
    return {
      title: 'Post Not Found',
      description: 'This blog post could not be found.',
    };
  }
  
  return {
    title: `${post.title} | Sudarshan's Blog`,
    description: post.description,
  };
}

export async function generateStaticParams() {
  const paths = getAllPostSlugs();
  return paths;
}

export default async function BlogPostPage({ params }: Params) {
  const post = getPostBySlug(params.slug);
  
  if (!post) {
    notFound();
  }
  
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
      
      <article className="prose prose-lg max-w-none prose-headings:font-semibold prose-a:text-blue-600 hover:prose-a:text-blue-800 prose-code:before:content-none prose-code:after:content-none prose-code:font-normal prose-code:bg-gray-100 prose-code:px-1 prose-code:py-0.5 prose-code:rounded">
        <header className="mb-8 border-b pb-4">
          <h1 className="text-4xl font-bold mb-2 !mt-0">{post.title}</h1>
          <div className="text-gray-500 text-base">
            Published on {formatDate(post.date)}
          </div>
          
          {post.tags && post.tags.length > 0 && (
            <div className="flex flex-wrap gap-2 mt-4">
              {post.tags.map((tag: string) => (
                <span key={tag} className="bg-gray-200 text-gray-700 px-2.5 py-0.5 rounded-full text-sm font-medium">
                  {tag}
                </span>
              ))}
            </div>
          )}
        </header>
        
        <MDXRemote source={post.content} />
      </article>
    </div>
  );
} 