// 画面のボタンアクションを管理する

/**
 * 果物マスタ管理画面での削除
 * @param {number} fruit_id 果物ID
 */
function confirmDelete(fruit_id) {
  if (confirm("本当に削除しますか？")) {
    window.location.href = `/fruit-stock-app/delete_fruit_master/${fruit_id}/`;
  }
}


/**
 * 販売情報管理画面での削除
 * @param {number} sales_id SalesID
 */
function confirmDelete(sales_id) {
  if (confirm("Are you sure you want to delete this fruit?")) {
    window.location.href = `/fruit-stock-app/delete_fruit_sales/${sales_id}/`;
  }
}
