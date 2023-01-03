
function loadItems(){
    return fetch('data/json')
    .then(response => response.json()) // data 성공적이면 json으로 반환
    .then(json => json.items); // json 안의 items 반환
}




loadItems()
.then(items => {
    displayItems(items);
    setEventListeners(items)
})
.catch(console.log)
