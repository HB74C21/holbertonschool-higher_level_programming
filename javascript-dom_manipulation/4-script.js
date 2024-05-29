document.getElementById('add_item').onclick = function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('ul.my_list').appendChild(newItem);
  };
