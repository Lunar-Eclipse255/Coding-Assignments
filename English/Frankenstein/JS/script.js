document.addEventListener('DOMContentLoaded', function () {
    const articles = [
        { title: 'Trial of Justine Moritz', content: 'Content for Article 1'},
        { title: 'Murder of Henry Clerval', content: 'Content for Article 2' },
        { title: 'From Marriage to Death: Murder of Elizabeth Frankenstein', content: 'Content for Article 3'},
        { title: 'Scientist Gone Mad', content: 'Content for Article 4' },
        { title: 'Letters to the Editor', content: 'Content for Article 5'},
        { title: 'Obituaries', content: 'Content for Article 6' },
        { title: 'Personals', content: 'Content for Article 7'},
        { title: 'Travel', content: 'Content for Article 8' },
        { title: 'Gossip', content: 'Content for Article 9'},
        { title: 'Citations', content: 'Content for Article 10'}
    ];

    const articleContainer = document.getElementById('article-container');

    articles.forEach((article, index) => {
        const articleSquare = document.createElement('div');
        articleSquare.classList.add('article-square');
        articleSquare.innerHTML = `<h3>${article.title}</h3>`;

        articleSquare.addEventListener('click', function () {
            window.location.href = `article${index + 1}.html`;
        });

        articleContainer.appendChild(articleSquare);
    });
});
document.getElementById('dynamic-footer').innerHTML = '<p>&copy;(Powered by Electricity)</p>';

