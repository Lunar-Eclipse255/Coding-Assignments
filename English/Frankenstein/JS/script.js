document.addEventListener('DOMContentLoaded', function () {
    const articles = [
        { title: 'Trial of Justine Moritz', content: 'Content for Article 1', imageSrc: "../Images/Trial.png" },
        { title: 'Murder of Henry Clerval', content: 'Content for Article 2',imageSrc: "../Images/Clarvel.png" },
        { title: 'From Marriage to Death: Murder of Elizabeth Frankenstein', content: 'Content for Article 3',imageSrc: "../Images/Murder.png"},
        { title: 'Genevan Scientist Gone', content: 'Content for Article 4',imageSrc: "../Images/Fled.png"},
        { title: 'Letters to the Editor', content: 'Content for Article 5',imageSrc: "../Images/Creation.png"},
        { title: 'Obituaries', content: 'Content for Article 6',imageSrc: "../Images/Alphonse.png"},
        { title: 'Personals', content: 'Content for Article 7',imageSrc: "../Images/Walton.png"},
        { title: 'Travel', content: 'Content for Article 8',imageSrc: "../Images/Arctic.png"},
        { title: 'Gossip', content: 'Content for Article 9',imageSrc: "../Images/Gossip.png"},
        { title: 'Citations', content: 'Content for Article 10',imageSrc: "../Images/Books.png"}
    ];

    const articleContainer = document.getElementById('article-container');

    articles.forEach((article, index) => {
        const articleSquare = document.createElement('div');
        articleSquare.classList.add('article-square');

        // Add image above h3
        const img = document.createElement('img');
        img.src = article.imageSrc;
        articleSquare.appendChild(img);

        // Add title
        const title = document.createElement('h3');
        title.textContent = article.title;
        articleSquare.appendChild(title);

        articleSquare.addEventListener('click', function () {
            window.location.href = `article${index + 1}.html`;
        });

        articleContainer.appendChild(articleSquare);
    });
});

document.getElementById('dynamic-footer').innerHTML = '<p>(Powered by Electricity)</p>';

