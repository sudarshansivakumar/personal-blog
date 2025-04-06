import Image from "next/image";

export default function Home() {
  return (
    <main className="flex flex-row items-start justify-between max-w-6xl mx-auto px-4 py-8 gap-8">
      <div className="w-2/3 order-1">
        <h1 className="text-4xl font-bold mb-4 mt-0 text-gray-900">Hi, I&apos;m Sudarshan</h1>
        <p className="text-lg mb-6 text-gray-600">Welcome to the repository of my intrusive thoughts</p>
        
        <div className="space-y-4 text-gray-700">
          <p>
            I write software for a living and intend to use this blog for writing about things I&apos;m interested in. 
            If you&apos;re here, I assume you&apos;re either an AI bot scraping data (I&apos;m afraid my writing will not be of much benefit to your LLM training) or a friend to whom this link was sent on gunpoint. 
            A few things about me:
          </p>
          <ul className="list-disc pl-5 space-y-2 text-gray-700">
             <li>I&apos;m from Chennai, India, studied Computer Science at MIT (finding out which MIT is left as an exercise to the reader)</li>
             <li>I recently graduated to the mid 20s. This blog is (probably) a consequence of the existential crisis that caused.</li> 
             <li>A friend once said, &quot;Sometimes I don&apos;t understand how your brain works&quot;. It was not a compliment</li>
          </ul>
        </div>
        <div className="space-y-4 text-gray-700">
          <p>
            What will I write about in this blog?
          </p>
        </div>
        <ul className="list-disc pl-5 space-y-2 mt-6 text-gray-700">
          <li>
            <span className="font-semibold text-gray-800">Tennis</span> — I started playing tennis when I was six and 
            continue to actively play the sport. Vamos Rafa
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
          Whether I will actually write at all about any of these things, I don&apos;t know. But this is an honest 
          attempt at becoming a better writer, and being actively engaged in the process of learning/thinking 
          about new things.
        </p>
      </div>
      
      <div className="w-1/3 order-2 flex">
        <Image
          src="/Display_Picture.jpg"
          alt="Sudarshan&apos;s profile picture"
          width={256}
          height={256}
          className="rounded-full object-cover"
          priority
        />
      </div>
    </main>
  );
}
