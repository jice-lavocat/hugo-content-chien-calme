*Using categories*

Each page can become a category and list several related articles in its bottom block. To turn a regular page into a category, just add the following metadata in the file :
    collection: category_slug

An article can be listed in one or several Categories. To achieve that, you should use metatags in the following syntax :
    categories: ["category_slug"]

If you want the article to be listed in several categories :
    categories: ["category_slug_1", "category_slug_2"]


Available categories :
    * Questions :
        - combien
        - comment
        - pourquoi
        - quand
        - que_faire

    * Activites :
        - activite_appartement
        - activite_eau
        - activite_montagne
        - activite_ville
        - activite_campagne

    * Techniques
        - massage
        - acuponcture
        - hypnose
        - osteopathie

    * Produits
        - produits



*Grandes images*
Pour les grandes images qui débordent du template, il faut ajouter la class 'img-responsive' à l'image pour que la largeur s'adapte au conteneur.

Exemple image qui dépasse :
<p align="center"><img src="/images/actualites/canicross-cynthia1.jpg"></p>

Exemple image reponsive :
<p align="center"><img src="/images/actualites/canicross-cynthia1.jpg" class="img-responsive"></p>

Template de base:
http://bootstrapbay.com/preview/blogdesk-responsive-html-blog-theme-B96B68E
http://www.mirchu.net/themes/BlogDesk/index.php
Design sympa: https://dogvacay.com/blog/
