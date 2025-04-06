import Image from "next/image";
import Link from "next/link";

export default function Home() {
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

      <main className="flex flex-col-reverse md:flex-row items-center md:items-start justify-between">
        <div className="md:pr-10 md:w-2/3">
          <h1 className="text-4xl font-bold mb-4">Hi, I'm Sudarshan</h1>
          <p className="text-lg mb-6">Welcome to the repository of my intrusive thoughts</p>
          
          <p className="mb-4">
            I write software for a living and currently work at{" "}
            <a href="https://clearfeed.com" className="text-blue-600 hover:underline">
              Clearfeed
            </a>{" "}
            as an AI/ML Engineer. I joined Clearfeed as an intern in my eighth semester 
            of undergrad and have since been building the NLP pipeline that drives our product!
          </p>
          
          <p className="mb-6">
            Anyway, this website won't be too much about my work. A long list of (inexhaustive) things 
            that I am interested in and hope to write about here:
          </p>
          
          <ul className="list-disc pl-6 space-y-6">
            <li>
              <span className="font-semibold">Tennis</span> — I started playing tennis when I was six and 
              continue to actively play the sport. I also (obsessively) follow the sport, and spend more 
              time thinking about it than I'd like to admit
            </li>
            <li>
              <span className="font-semibold">Technology/Software</span> — I am pretty early in my career 
              as a software developer and intend to write about things that I learn along the way. It's also 
              a particularly interesting time to be working in AI (more than half the code for this site was 
              written by an LLM)
            </li>
            <li>
              <span className="font-semibold">Society/Politics/Culture</span> — I have several (possibly incorrect) 
              opinions about the times we live in. While I am not brave enough to broadcast some of them publicly, 
              I will attempt to put out what I can
            </li>
            <li>
              <span className="font-semibold">Media/Literature</span> — I like reading and watching movies/TV Shows 
              (my Instagram screen time might suggest otherwise).
            </li>
          </ul>
          
          <p className="mt-6">
            Whether I will actually write at all about any of these things, I do not know. But this is an honest 
            attempt at becoming a better writer, and being actively engaged in the process of learning/thinking 
            about new things.
          </p>
        </div>
        
        <div className="md:w-1/3 flex justify-center mb-8 md:mb-0">
          <div className="rounded-full overflow-hidden w-64 h-64">
            <Image
              src="/Display_Picture.jpg"
              alt="Sudarshan's profile picture"
              width={300}
              height={300}
              className="object-cover"
              priority
            />
          </div>
        </div>
      </main>
    </div>
  );
}
