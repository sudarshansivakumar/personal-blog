import React from 'react';
import { MDXRemote, MDXRemoteSerializeResult } from 'next-mdx-remote';

interface MarkdownRendererProps {
  content: MDXRemoteSerializeResult;
}

const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({ content }) => {
  return <MDXRemote {...content} />;
};

export default MarkdownRenderer; 