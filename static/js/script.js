"use strict";







var myModal = new bootstrap.Modal(document.getElementById('exampleModalCenter'), {
    keyboard: false
});

// Функция для открытия модального окна и вывода id кнопки внутрь содержимого модального окна
function openModal(buttonId) {
    var button = document.getElementById(buttonId);
    var buttonIdText = button.textContent;
    document.getElementById('modalBodyContent').textContent = buttonIdText;
    myModal.show();
}



// Добавляем обработчик события для каждой кнопки
document.getElementById('button1').addEventListener('click', function() {
    openModal('button1');
});

document.getElementById('button2').addEventListener('click', function() {
    openModal('button2');
});
document.addEventListener("DOMContentLoaded", function() {
    // Слушаем событие при закрытии модального окна с аудио
    $('#exampleModalCenter2').on('namehidden.bs.modal', function (e) {
      let video = document.getElementById('Video');
      let videoPlayer = video.querySelector('video');
      videoPlayer.pause(); 
    });

    $('#exampleModalCenter1').on('hidden.bs.modal', function (e) {
      let audio = document.getElementById('Audio');
      let audioPlayer = audio.querySelector('audio');
      audioPlayer.pause(); 
    });
  });
  $('#exampleModalCenter2').on('hidden.bs.modal', function (e) {
    let video = document.getElementById('Video');
    let videoPlayer = video.querySelector('video');
    videoPlayer.pause(); 
  });

  $('#exampleModalCenter1').on('hidden.bs.modal', function (e) {
    let audio = document.getElementById('Audio');
    let audioPlayer = audio.querySelector('audio');
    audioPlayer.pause(); 
  });