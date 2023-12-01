function toggleFields() {
    const type = document.querySelector('select[name="type"]').value;
    const debitGroup = document.getElementById('debit-group');
    console.log(type)
    const creditGroup = document.getElementById('credit-group');

    if (type === 'debit') {
        creditGroup.style.display = 'none !important';
        debitGroup.style.display = 'block !important';
    } else {
        creditGroup.style.display = 'block !important';
        debitGroup.style.display = 'none !important';
    }
}

toggleFields(); 