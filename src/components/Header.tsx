import Link from 'next/link';

const Header = () => {
  return (
    <header className="bg-white border-b border-gray-200">
      <nav className="container mx-auto px-4 py-4 flex justify-center items-center">
        <Link href="/" className="text-gray-800 hover:text-blue-600 font-medium mr-4">
          Home
        </Link>
        <span className="text-gray-400 mr-4">|</span> {/* Separator */}
        <Link href="/blog" className="text-gray-800 hover:text-blue-600 font-medium">
          Blog
        </Link>
      </nav>
    </header>
  );
};

export default Header; 