<script lang="ts">
  // SvelteKit page component for the homepage
</script>

<div class="container">
  <main class="main-content">
    <div class="intro-grid">
      <div class="intro-text">
        <h1>Hi, I'm Sudarshan</h1>
        <h2>Welcome to the repository of my intrusive thoughts</h2>

        <p>
          I write software for a living and currently work at <a href="https://clearfeed.ai" target="_blank" rel="noopener noreferrer">Clearfeed</a> as an AI/ML
          Engineer. I joined Clearfeed as an intern in my eighth semester of
          undergrad and have since been building the NLP pipeline that drives our
          product!
        </p>

        <p>
          Anyway, this website won't be too much about my work. A long list of
          (inexhaustive) things that I am interested in and hope to write about here:
        </p>

        <ul>
          <li>
            <strong>Tennis</strong> — I started playing tennis when I was six and continue to actively play the sport. I also (obsessively)
            follow the sport, and spend more time thinking about it than I'd like to admit
          </li>
          <li>
            <strong>Technology/Software</strong> — I am pretty early in my career as a software developer and intend to write about
            things that I learn along the way. It's also a particularly interesting time to be working in AI (more than half
            the code for this site was written by an LLM)
          </li>
          <li>
            <strong>Society/Politics/Culture</strong>— I have several (possibly incorrect) opinions about the times we live in. While I am
            not brave enough to broadcast some of them publicly, I will attempt to put out what I can
          </li>
          <li>
            <strong>Media/Literature</strong>— I like reading and watching movies/TV Shows (my Instagram screen time might suggest
            otherwise).
          </li>
        </ul>

        <p>
          Whether I will actually write at all about any of these things, I do not know. But this is an honest
          attempt at becoming a better writer, and being actively engaged in the process of learning/thinking
          about new things.
        </p>

      </div>
      <div class="intro-image">
        <img src="/Display_Picture.jpg" alt="Sudarshan Sivakumar" class="profile-pic" />
      </div>
    </div>
      <footer class="quote">
          <p><em>"I am large. I contain multitudes."</em> - Walt Whitman</p>
      </footer>
  </main>
</div>

<style>
  /* Basic Styles - We can refine these or use a framework later */
  .container {
    max-width: 1150px; /* Slightly wider container */
    margin: 1.5rem auto; /* Reduced top/bottom margin */
    padding: 0 1.5rem;
    font-family: 'Georgia', serif; /* Basic serif font */
    line-height: 1.55; /* Slightly tighter line-height */
    color: #333;
    font-size: 0.95rem; /* Keep base font size */
  }

  .main-content {
      padding-top: 1rem; /* Reduced top padding */
  }

  .intro-grid {
    display: grid;
    grid-template-columns: 2.5fr 1fr; /* Give text more relative width */
    gap: 2rem; /* Reduced gap */
    align-items: start;
  }

  .intro-text h1 {
    font-size: 2.3rem; /* Slightly smaller h1 */
    margin-bottom: 0.3rem;
    font-weight: normal;
    color: #222;
    line-height: 1.2;
  }

  .intro-text h2 {
    font-size: 1.25rem; /* Slightly smaller h2 */
    font-weight: normal;
    color: #555;
    margin-bottom: 1.3rem; /* Reduced margin */
    border-bottom: none; /* Override potential global styles */
  }

  .intro-text p {
    font-size: 0.98rem; /* Slightly smaller p */
    margin-bottom: 1.1rem; /* Reduced margin */
  }

    .intro-text a {
        color: #007bff; /* Standard link blue */
        text-decoration: none;
    }

    .intro-text a:hover {
        text-decoration: underline;
    }

  .intro-text ul {
    list-style: disc;
    padding-left: 25px; /* Indent list */
    margin-bottom: 1.2rem; /* Reduced margin */
  }

  .intro-text li {
    margin-bottom: 0.7rem; /* Reduced margin */
    font-size: 0.95rem; /* Reduced li size */
    color: #444;
  }

    .intro-text li strong {
        font-weight: bold;
        color: #111;
    }

  .intro-image {
    text-align: center; /* Center image if container is wider */
  }

  .profile-pic {
    max-width: 280px; /* Reduce max image width */
    height: auto;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 50%;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08); /* Slightly reduced shadow */
  }

    .quote {
        text-align: center;
        margin-top: 2.5rem; /* Reduced margin */
        padding-top: 1.5rem;
        border-top: 1px solid #eee;
        font-size: 1rem;
        color: #666;
    }

  /* Responsive adjustments */
  @media (max-width: 768px) {
    .intro-grid {
      grid-template-columns: 1fr; /* Stack columns on smaller screens */
      gap: 1.5rem;
    }
    .intro-image {
      order: -1; /* Move image to the top on mobile */
      margin-bottom: 1.5rem;
    }
        .profile-pic {
            max-width: 180px; /* Adjusted mobile size */
        }
    .intro-text h1 {
        font-size: 2rem;
    }
    .intro-text h2 {
        font-size: 1.2rem;
    }
  }
</style>
