function _getItemList(arr) {
    let itemList = [];
    for (const itemArr of arr) {
        itemList.push(itemArr[1]);
    }

    return itemList;
}


function _findAlphabeticalIndex(existingInvArr, newItem) {
    const existingItems = _getItemList(existingInvArr);
    for (const item in existingItems) {
        if (newItem < existingItems[item])
            return item;
    }

    return existingItems.length;

}


function updateInventory(arr1, arr2) {
    
    
    for (const itemNew of arr2) {
        let itemExists = 0;
        for (const itemExisting of arr1) {
            if (itemExisting[1] == itemNew[1]) {
                itemExisting[0] = itemExisting[0] + itemNew[0]; 
                itemExists = 1;
            }
        }
        if (itemExists == 0) {
            arr1.splice(_findAlphabeticalIndex(arr1, itemNew[1]), 0, itemNew)
        }
    }
    console.log(arr1);
    return arr1;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
