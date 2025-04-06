import Image from "next/image";

export default function Home() {
  return (
    <main className="flex flex-row items-start justify-between max-w-6xl mx-auto px-4 py-8 gap-8">
      <div className="w-2/3 order-1">
        <h1 className="text-4xl font-bold mb-4 mt-0 text-gray-900">Hi, I&apos;m Sudarshan</h1>
        <p className="text-lg mb-6 text-gray-600">Welcome to the repository of my intrusive thoughts</p>
        
        <div className="space-y-4 text-gray-700">
          <p>
            I write software for a living and currently work at{" "}
            <a href="https://clearfeed.ai" className="text-blue-600 hover:underline font-medium">
              Clearfeed
            </a>{" "}
            as an AI/ML Engineer. I joined Clearfeed as an intern in my eighth semester 
            of undergrad and have since been building the NLP pipeline that drives our product!
          </p>
          
          <p>
            Anyway, this website won&apos;t be too much about my work. A long list of (inexhaustive) things 
            that I am interested in and hope to write about here:
          </p>
        </div>
        
        <ul className="list-disc pl-5 space-y-2 mt-6 text-gray-700">
          <li>
            <span className="font-semibold text-gray-800">Tennis</span> — I started playing tennis when I was six and 
            continue to actively play the sport. I also (obsessively) follow the sport, and spend more 
            time thinking about it than I&apos;d like to admit
          </li>
          <li>
            <span className="font-semibold text-gray-800">Technology/Software</span> — I am pretty early in my career 
            as a software developer and intend to write about things that I learn along the way. It&apos;s also 
            a particularly interesting time to be working in AI (more than half the code for this site was 
            written by an LLM)
          </li>
          <li>
            <span className="font-semibold text-gray-800">Society/Politics/Culture</span> — I have several (possibly incorrect) 
            opinions about the times we live in. While I am not brave enough to broadcast some of them publicly, 
            I will attempt to put out what I can
          </li>
          <li>
            <span className="font-semibold text-gray-800">Media/Literature</span> — I like reading and watching movies/TV Shows 
            (my Instagram screen time might suggest otherwise).
          </li>
        </ul>
        
        <p className="mt-6 text-gray-700">
          Whether I will actually write at all about any of these things, I do not know. But this is an honest 
          attempt at becoming a better writer, and being actively engaged in the process of learning/thinking 
          about new things.
        </p>
      </div>
      
      <div className="w-1/3 order-2 flex">
        <Image
          src="/Display_Picture.jpg"
          alt="Sudarshan's profile picture"
          width={256}
          height={256}
          className="rounded-full object-cover"
          priority
        />
      </div>
    </main>
  );
}
