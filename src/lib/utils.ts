export function formatDate(dateString: string): string {
  const date = new Date(dateString);
  
  // Format: Month Day, Year (e.g., January 1, 2023)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
} 