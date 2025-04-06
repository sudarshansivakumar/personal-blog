import { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getAllPostSlugs, getPostBySlug } from '@/lib/blog';
import { formatDate } from '@/lib/utils';
import { MDXRemote } from 'next-mdx-remote/rsc';
import remarkGfm from 'remark-gfm';
import Tag from '@/components/Tag';

const options = {
  mdxOptions: {
    remarkPlugins: [remarkGfm],
    rehypePlugins: [],
  },
};

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const resolvedParams = await params;
  const slug = resolvedParams.slug;
  const post = await getPostBySlug(slug);

  if (!post) {
    return {
      title: 'Post Not Found',
      description: 'The requested blog post could not be found',
      icons: {
        icon: [
          { url: '/icon.png', type: 'image/png' },
          { url: '/icon.png', type: 'image/x-icon' }
        ],
      },
    };
  }
  
  return {
    title: post.title,
    description: post.description || `Blog post about ${post.title}`,
    icons: {
      icon: [
        { url: '/icon.png', type: 'image/png' },
        { url: '/icon.png', type: 'image/x-icon' }
      ],
    },
  };
}

export function generateStaticParams() {
  const paths = getAllPostSlugs();
  return paths;
}

export default async function BlogPostPage({ params }: Props) {
  const resolvedParams = await params;
  const post = await getPostBySlug(resolvedParams.slug);
  
  if (!post) {
    notFound();
  }
  
  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <article className="prose prose-lg max-w-none prose-headings:font-semibold prose-a:text-blue-600 hover:prose-a:text-blue-800 prose-code:before:content-none prose-code:after:content-none prose-code:font-normal prose-code:bg-gray-100 prose-code:px-1 prose-code:py-0.5 prose-code:rounded">
        <header className="mb-8 border-b pb-4">
          <h1 className="text-4xl font-bold mb-2 !mt-0">{post.title}</h1>
          <div className="text-gray-500 text-base">
            Published on {formatDate(post.date)}
          </div>
          
          {post.tags && post.tags.length > 0 && (
            <div className="mt-4">
              {post.tags.map((tag) => (
                <Tag key={tag} name={tag} />
              ))}
            </div>
          )}
        </header>
        
        <MDXRemote source={post.content} options={options} />
      </article>
    </div>
  );
} 