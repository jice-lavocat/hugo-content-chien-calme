## Using categories

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



## Grandes images

Pour les grandes images qui débordent du template, il faut ajouter la class 'img-responsive' à l'image pour que la largeur s'adapte au conteneur.

Exemple image qui dépasse :
<p align="center"><img src="/images/actualites/canicross-cynthia1.jpg"></p>

Exemple image reponsive :
<p align="center"><img src="/images/actualites/canicross-cynthia1.jpg" class="img-responsive"></p>


# Faire un lien interne
Une base de liens internes est accessible via l'utilisation d'un shortcode. Voici comment y accéder :

    {{< link target="tomate" title="Tomates" >}}

Fera un lien vers la page cible `target` avec l'ancre `title`.

Si l'ancre `title` n'est pas présente, l'ancre utilisée sera identique au mot clé `target`.

Les liens utilisable sont disponibles dans le fichier /layout/shortcodes/link.html

Si un lien target n'est pas disponible, le shortcode renverra uniquement `title`  (ou  `target` si title n'est pas défini).

Exemple:
{{< link target="banane" title="Bananes" >}}
    renvoie : <a href="/aliments/fruits/banane/">Bananes</a>

{{< link target="banane" >}}
    renvoie : <a href="/aliments/fruits/banane/">banane</a>

## Template de base:
http://bootstrapbay.com/preview/blogdesk-responsive-html-blog-theme-B96B68E
http://www.mirchu.net/themes/BlogDesk/index.php
Design sympa: https://dogvacay.com/blog/
