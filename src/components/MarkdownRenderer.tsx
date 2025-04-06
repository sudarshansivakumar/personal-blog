import React from 'react';
import { MDXRemote } from 'next-mdx-remote';

interface MarkdownRendererProps {
  content: any;
}

const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({ content }) => {
  return <MDXRemote {...content} />;
};

export default MarkdownRenderer; 