<script lang="ts">
  // Root layout component
  import './styles.css'; // Optional: If you want global styles
</script>

<div class="layout-container">
  <nav class="main-nav">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/blog">Blog</a></li>
      <!-- Add other links here if needed -->
    </ul>
  </nav>

  <main class="layout-main-content">
    <slot /> <!-- Page content will be injected here -->
  </main>

  <!-- You could add a footer here as well -->

</div>

<style>
  /* Basic Layout & Nav Styles */
  .layout-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh; /* Ensure layout takes full viewport height */
    font-family: sans-serif; /* Apply a base font */
  }

  .main-nav {
    background-color: #f8f8f8;
    border-bottom: 1px solid #e0e0e0;
    padding: 0.8rem 1.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  .main-nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    gap: 1.5rem;
    max-width: 1100px; /* Align with homepage container */
    margin: 0 auto; /* Center nav items */
  }

  .main-nav a {
    text-decoration: none;
    color: #333;
    font-weight: 600;
    font-size: 0.95rem;
    transition: color 0.2s ease;
  }

  .main-nav a:hover,
  .main-nav a[aria-current='page'] /* Style for active link */
  {
    color: #007bff; /* Highlight color */
  }

  .layout-main-content {
    flex-grow: 1; /* Allow main content to fill available space */
    /* Padding/margin for main content is handled by individual page containers */
  }

  /* Optional: Create src/routes/styles.css for global styles */

</style> 