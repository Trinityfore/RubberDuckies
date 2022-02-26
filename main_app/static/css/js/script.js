// Date picker animation

const dateEl = document.getElementById('id_date');
const selectEl = document.getElementById('id_meal');


M.Datepicker.init(dateEl, {
    format: 'yyyy-mm-dd', 
    defaultDate: new Date(),
    setDefaultDate: true,
    autoClose:true
});

M.FormSelect.init(selectEl); 