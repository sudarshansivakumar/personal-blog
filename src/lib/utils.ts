// Helper function to format date
export function formatDate(dateString: string): string {
  try {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  } catch (e) {
    console.error("Error formatting date:", dateString, e);
    return dateString; // Fallback to original string or consider 'Invalid Date'
  }
} 