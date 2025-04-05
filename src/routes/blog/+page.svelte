<script lang="ts">
  import type { PageData } from './$types';

  export let data: PageData;

  // Helper function to format date (optional, can be customized)
  function formatDate(dateString: string) {
    try {
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    } catch (e) {
      console.error("Error formatting date:", dateString, e);
      return dateString; // Fallback to original string
    }
  }
</script>

<div class="container blog-list-page">
  <h1>Blog Posts</h1>
  <p class="collection-desc">A collection of my various ramblings</p>

  {#if data.posts && data.posts.length > 0}
    <ul class="blog-list">
      {#each data.posts as post}
        <li class="blog-item">
          <h3>
            <a href={"/blog/" + post.slug}>{post.title}</a>
          </h3>
          {#if post.description}
            <p class="blog-desc">{post.description}</p>
          {/if}
          <p class="blog-meta">
            Published on {formatDate(post.date)}
            {#if post.tags && post.tags.length > 0}
              <span class="tag-separator">|</span> Tags:
              <span class="tag-container">
                {#each post.tags as tag}
                  <span class="tag">{tag}</span>
                {/each}
              </span>
            {/if}
          </p>
        </li>
      {/each}
    </ul>
  {:else}
    <p>I promise, there will be some writing here very soon</p>
  {/if}
</div>

<style>
  .container.blog-list-page {
    max-width: 900px;
    margin: 2rem auto;
    padding: 0 1.5rem;
    font-family: 'Georgia', serif;
    color: #333;
  }

  h1 {
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
    font-weight: normal;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.5rem;
  }

  .collection-desc {
      font-size: 1.1rem;
      color: #666;
      margin-bottom: 2.5rem;
      font-style: italic;
  }

  .blog-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .blog-item {
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid #eee;
  }

  .blog-item:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
  }

  .blog-item h3 {
    font-size: 1.6rem;
    margin: 0 0 0.5rem 0;
    font-weight: bold;
    line-height: 1.3;
  }

  .blog-item h3 a {
    text-decoration: none;
    color: #222;
    transition: color 0.2s ease-in-out;
  }

  .blog-item h3 a:hover {
    color: #007bff; /* Or your accent color */
  }

  .blog-desc {
    font-size: 1rem;
    color: #555;
    margin: 0 0 0.8rem 0;
    line-height: 1.6;
  }

  .blog-meta {
    font-size: 0.85rem;
    color: #777;
    font-family: sans-serif; /* Use sans-serif for meta data */
  }

  .tag-separator {
      margin: 0 0.5em;
  }

  .tag-container {
    display: inline-flex; /* Keep tags on the same line if possible */
    flex-wrap: wrap; /* Allow wrapping if too many tags */
    gap: 0.4rem;
    margin-left: 0.3rem; /* Small space after 'Tags:' */
    vertical-align: middle; /* Align tags nicely with text */
  }

  .tag {
    background-color: #f0f0f0;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    color: #555;
    white-space: nowrap; /* Prevent tags breaking mid-word */
  }
</style> 