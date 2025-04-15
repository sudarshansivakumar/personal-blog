import Image from "next/image";

export default function Home() {
  return (
    <main className="max-w-2xl mx-auto px-6 py-12">
      <div className="w-full">
        <h2 className="mb-3 mt-0">Hi, I&apos;m Sudarshan</h2>
        <p className="text-lg mb-8 text-gray-700 italic">Welcome to the repository of my intrusive thoughts</p>
        
        <div className="space-y-6">
          <p>
            If you&apos;re here, I assume you&apos;re either an AI bot scraping data (I&apos;m afraid my writing will not be of much benefit to your LLM training) or a friend to whom this link was forcibly shared. 
            A few things about me:
          </p>
          <ul className="list-disc pl-5 space-y-2">
             <li>I&apos;m from Chennai, India, and studied Computer Science at MIT (finding out which MIT is left as an exercise to the reader)</li>
             <li>I recently graduated to the mid 20s. This blog is (probably) a consequence of the existential crisis that caused.</li> 
             <li>A friend once said, &quot;Sometimes I don&apos;t understand how your brain works&quot;. It was not a compliment</li>
          </ul>
        </div>
        <div className="mt-10">
          <h4 className="mb-4">What will I write about in this blog?</h4>
        </div>       
        <p className="mt-8">
         I would like to hope I can write about things that are meaningful to me and would speak to a large number of people  
        </p>
        <p>
        Maybe something political that I have been thinking about, or what it means to navigate the world in your 20s in times that are increasingly uncertain.
        In all honesty though - I know as much about what this blog will be about as I know about my purpose in this universe. 
        </p>
        <p>
        More than anything else, I want to use this platform to become a better writer and talk about things that I find interesting and/or am thinking about. 
        </p>

        
      </div>
    </main>
  );
}
