var baseURL = 'http://localhost:8000/';

var numberAInp = $('#numberA');
var numberBInp = $('#numberB');
var addBtn = $('#addBtn');
var subtractBtn = $('#subtractBtn');
var multiplyBtn = $('#multiplyBtn');
var divideBtn = $('#divideBtn');
var result = $('#result');

var showResult = function (response) {
    result.html(response);
};

var calc = function(action) {
    var numberA = numberAInp.val();
    var numberB = numberBInp.val();
    $.ajax({
        method: 'POST',
        url: baseURL + action,
        data: {a: numberA, b: numberB},
        success: function (response) {
            showResult(response);
        },
        error: function (error) {
            $.alert(error);
        }
    });
};

addBtn.on('click', function () {
    calc('add');
});
subtractBtn.on('click', function () {
    calc('subtract');
});
multiplyBtn.on('click', function () {
    calc('multiply');
});
divideBtn.on('click', function () {
    calc('divide');
});




//
//
// const indexLink = 'http://localhost:8000/add/';
//
// // $(document.createElement('div'))
//
// function renderData(data) {
//         const container = $('.container');
//     let countryDiv = $(document.createElement('div'));
//     countryDiv.addClass('answer');
//     // countryDiv.append(`<a href="index.html">Назад</a></br>`);
//     countryDiv.append(`<h1>${data.A}</h1></br>`);
//     // countryDiv.append(`<img src="${data.flag}" alt="Флаг" style="height: 100px"><br><br>`);
//     countryDiv.append(`Код: ${data.B}<br>`);
//     // countryDiv.append(`Валюта: ${data.currencies[0]['code']}<br>`);
//     // countryDiv.append(`Население: ${data.population}<br>`);
// }
//
// function jqueryParseData (response, status) {
//     console.log(response);
//     console.log(status);
//     renderData(response);
// }
//
// function jqueryAjaxError(response, status) {
//     console.log(response);
//     console.log(status);
//     console.log('error');
// }
//
// function jqueryLoadIndex() {
//     $.ajax({
//         url: indexLink,
//         method: 'POST',
//         data: {"A": 1234, "B": 4567},
//         success: jqueryParseData,
//         error: jqueryAjaxError
//     })
// }
//
// $(document).ready(function () {
//    data = jqueryLoadIndex();
// });
