function confirmDelete(fruit_id) {
  if (confirm("Are you sure you want to delete this fruit?")) {
    window.location.href = `/fruit-stock-app/delete_fruit_master/${fruit_id}/`;
  }
}
