
function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json()) // data 성공적이면 json으로 반환
    .then(json => json.items); // json 안의 items 반환
}

function displayItems(items){
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

function createHTMLString(item){
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumnail">
        <span class="item_description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function onButtonClick(event, items){
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key==null || value ==null){
        return;
    }

    
    displayItems(items.filter(item=>item[key] === value));
}


function setEventListeners(items){
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(Items));
    buttons.addEventListener('click', event => onButtonClick(event, items));
}

loadItems()
.then(items => {
    displayItems(items);
    setEventListeners(items)
})
.catch(console.log)
