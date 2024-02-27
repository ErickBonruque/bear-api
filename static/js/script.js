// Seleção de elementos do DOM
const selectImage = document.querySelector('.select-image');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.img-area');

// Pegando o click do botão e disparando o click do input file
selectImage.addEventListener('click', function () {
    inputFile.click();
})

// Pegando o arquivo selecionado e mostrando na tela
inputFile.addEventListener('change', function () {
    const image = this.files[0]
    const reader = new FileReader();
    // Verificando se o arquivo é uma imagem
    reader.onload = () => {
        const allImg = imgArea.querySelectorAll('img');
        allImg.forEach(item => item.remove());
        const imgUrl = reader.result;
        const img = document.createElement('img');
        img.src = imgUrl;
        imgArea.appendChild(img);
        imgArea.classList.add('active');
        imgArea.dataset.img = image.name;

        console.log('Imagem:', image);
        // Passando a imagem para o "predict" do Flask
        //passImageToFlask(image);
    }
    // Lendo o arquivo
    reader.readAsDataURL(image);
})