import Link from 'next/link';

const Header = () => {
  return (
    <header className="border-b border-gray-200 py-4">
      <nav className="container mx-auto px-6 flex justify-center items-center">
        <Link href="/" className="hover:text-black tracking-widest text-gray-700 px-4">
          Home
        </Link>
        <span className="mx-3 text-gray-300">|</span>
        <Link href="/blog" className="hover:text-black tracking-widest text-gray-700 px-4">
          Blog
        </Link>
      </nav>
    </header>
  );
};

export default Header; 