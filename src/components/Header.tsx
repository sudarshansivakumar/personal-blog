import Link from 'next/link';

const Header = () => {
  return (
    <header className="border-b border-dark-border py-4">
      <nav className="container mx-auto px-6 flex justify-center items-center">
        <Link href="/" className="px-4">
          Home
        </Link>
        <span className="mx-3 text-dark-text-muted">|</span>
        <Link href="/blog" className="px-4">
          Blog
        </Link>
      </nav>
    </header>
  );
};

export default Header; 