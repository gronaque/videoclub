#from kivy.config import Config
#Config.set('graphics', 'fullscreen', 'auto')
#Config.set('graphics', 'borderless', '1')

import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior, DragBehavior
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
import os
import random
from kivy.uix.floatlayout import FloatLayout


FILM_FOLDER = "films"  # dossier où sont stockés les dossiers films

# Fixe une taille par défaut pour les tests sur ordinateur
Window.size = (600, 1024)

class ClickableImage(ButtonBehavior, Image):
    pass

def charger_films_par_annees():
    films = []
    dossier_films = "films"

    for nom_dossier in os.listdir(dossier_films):
        chemin = os.path.join(dossier_films, nom_dossier)
        if os.path.isdir(chemin):
            infos_path = os.path.join(chemin, "info.txt")
            if os.path.exists(infos_path):
                film = {"titre": nom_dossier, "chemin": chemin}
                with open(infos_path, "r", encoding="utf-8") as f:
                    for ligne in f:
                        ligne = ligne.strip()
                        if not ligne or ":" not in ligne:
                            continue
                        cle, valeur = ligne.split(":", 1)
                        cle = cle.strip().lower()
                        valeur = valeur.strip()
                        if cle == "annee":
                            film["annee"] = valeur
                if "annee" in film:
                    films.append(film)
                else:
                    print(f"[!] Pas d'année dans {infos_path}")
            else:
                print(f"[!] infos.txt manquant dans {chemin}")
    return films



class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Utiliser FloatLayout pour superposer widgets
        self.layout = FloatLayout()

        # Image de fond
        self.bg = Image(source='assets/fond.jpg',
                        allow_stretch=True,
                        keep_ratio=False,
                        size_hint=(1, 1),
                        pos_hint={'x': 0, 'y': 0})

        # Ajouter l’image de fond en premier (derrière)
        self.layout.add_widget(self.bg)

        # Conteneur principal pour le contenu de l’écran
        self.content = FloatLayout(size_hint=(1, 1))
        self.layout.add_widget(self.content)

        self.add_widget(self.layout)

class BaseScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Utiliser FloatLayout pour superposer widgets
        self.layout = FloatLayout()

        # Image de fond
        self.bg = Image(source='assets/fond2.jpg',
                        allow_stretch=True,
                        keep_ratio=False,
                        size_hint=(1, 1),
                        pos_hint={'x': 0, 'y': 0})

        # Ajouter l’image de fond en premier (derrière)
        self.layout.add_widget(self.bg)

        # Conteneur principal pour le contenu de l’écran
        self.content = FloatLayout(size_hint=(1, 1))
        self.layout.add_widget(self.content)

        self.add_widget(self.layout)

class BaseScreen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Utiliser FloatLayout pour superposer widgets
        self.layout = FloatLayout()

        # Image de fond
        self.bg = Image(source='assets/fond3.jpg',
                        allow_stretch=True,
                        keep_ratio=False,
                        size_hint=(1, 1),
                        pos_hint={'x': 0, 'y': 0})

        # Ajouter l’image de fond en premier (derrière)
        self.layout.add_widget(self.bg)

        # Conteneur principal pour le contenu de l’écran
        self.content = FloatLayout(size_hint=(1, 1))
        self.layout.add_widget(self.content)

        self.add_widget(self.layout)

class BaseScreen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Utiliser FloatLayout pour superposer widgets
        self.layout = FloatLayout()

        # Image de fond
        self.bg = Image(source='assets/fond4.jpg',
                        allow_stretch=True,
                        keep_ratio=False,
                        size_hint=(1, 1),
                        pos_hint={'x': 0, 'y': 0})

        # Ajouter l’image de fond en premier (derrière)
        self.layout.add_widget(self.bg)

        # Conteneur principal pour le contenu de l’écran
        self.content = FloatLayout(size_hint=(1, 1))
        self.layout.add_widget(self.content)

        self.add_widget(self.layout)





class IntroScreen(BaseScreen):
    def on_enter(self):
        Clock.schedule_once(self.goto_menu, 0)

    def goto_menu(self, dt):
        self.manager.current = "menu"

class MenuScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
	
        btn_search = Button(text="RECHECHE", size_hint=(1, 0.1))
        btn_search.background_normal = ''  # désactive l’image de fond par défaut
        btn_search.background_color = (1, 1, 1, 0.5)
        btn_search.font_name = 'assets/titres.ttf'
        btn_search.font_size = 35  # taille de police, par exemple 24 pixels
        btn_search.color = (0, 0, 0, 1)
        btn_search.bind(on_release=self.goto_search)
        layout.add_widget(btn_search)

        btn_tous = Button(text="TOUS LES FILMS", size_hint=(1, 0.1))
        btn_tous.background_normal = ''  # désactive l’image de fond par défaut
        btn_tous.background_color = (1, 1, 1, 0.5)
        btn_tous.font_name = 'assets/titres.ttf'
        btn_tous.font_size = 35  # taille de police, par exemple 24 pixels
        btn_tous.color = (0, 0, 0, 1)
        btn_tous.bind(on_release=self.goto_tous)
        layout.add_widget(btn_tous)

        btn_random = Button(text="AU HASARD", size_hint=(1, 0.1))
        btn_random.background_normal = ''  # désactive l’image de fond par défaut
        btn_random.background_color = (1, 1, 1, 0.5)
        btn_random.font_name = 'assets/titres.ttf'
        btn_random.font_size = 35  # taille de police, par exemple 24 pixels
        btn_random.color = (0, 0, 0, 1)
        btn_random.bind(on_release=self.goto_random)
        layout.add_widget(btn_random)

        btn_categories = Button(text="CATÉGORIES", size_hint=(1, 0.1))
        btn_categories.background_normal = ''  # désactive l’image de fond par défaut
        btn_categories.background_color = (1, 1, 1, 0.5)
        btn_categories.font_name = 'assets/titres.ttf'
        btn_categories.font_size = 35  # taille de police, par exemple 24 pixels
        btn_categories.color = (0, 0, 0, 1)
        btn_categories.bind(on_release=self.goto_categorie_choix)
        layout.add_widget(btn_categories)

        self.add_widget(layout)

    def goto_tous(self, instance):
        self.manager.get_screen("all_films").refresh_films()
        self.manager.current = "all_films"

    def goto_search(self, instance):
        self.manager.current = "search"

    def goto_random(self, instance):
        self.manager.get_screen("random_film").show_random_film()
        self.manager.current = "random_film"

    def goto_categorie_choix(self, instance):
        self.manager.current = "categorie_choix"


class AllFilmsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.films = []
        self.chrono_asc = True  # état du tri

        main_layout = BoxLayout(orientation="vertical")

        from kivy.uix.label import Label
        from kivy.uix.anchorlayout import AnchorLayout
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.bind(on_release=self.go_back)
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        main_layout.add_widget(anchor)
        
        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid_films = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.grid_films.bind(minimum_height=self.grid_films.setter('height'))

        self.scroll.add_widget(self.grid_films)
        main_layout.add_widget(self.scroll)

        self.add_widget(main_layout)

    def go_back(self, instance):
        self.manager.current = "categorie_choix"

    def load_films_from_folder(self):
        films = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        film_folder = os.path.join(base_dir, FILM_FOLDER)
        if not os.path.exists(film_folder):
            print(f"Le dossier {film_folder} n'existe pas.")
            return films

        for folder_name in os.listdir(film_folder):
            folder_path = os.path.join(film_folder, folder_name)
            if os.path.isdir(folder_path):
                info_path = os.path.join(folder_path, "info.txt")
                if os.path.isfile(info_path):
                    film_info = {}
                    try:
                        with open(info_path, "r", encoding="utf-8") as f:
                            for line in f:
                                if ":" in line:
                                    key, value = line.split(":", 1)
                                    film_info[key.strip()] = value.strip()
                        film_info["folder_path"] = folder_path
                        films.append(film_info)
                    except Exception as e:
                        print(f"Erreur lecture info.txt dans {folder_path} : {e}")
        return films

    def refresh_films(self):
        self.grid_films.clear_widgets()
        self.films = self.load_films_from_folder()
        if not self.films:
            print("Aucun film chargé.")
            return

        films_by_year = {}
        for film in self.films:
            annee = film.get("annee", "").strip()
            if annee:
                films_by_year.setdefault(annee, []).append(film)

        
            
        if not self.films:
            print("Aucun film chargé.")
            return
        for film in self.films:
            affiche_path = os.path.join(film["folder_path"], "affiche.jpg")
            if not os.path.isfile(affiche_path):
                print(f"Affiche introuvable pour {film.get('titre', 'titre inconnu')} : {affiche_path}")
                continue
            img = ClickableImage(source=affiche_path, size_hint_y=None, height=200, allow_stretch=True, keep_ratio=True)
            img.bind(on_release=lambda instance, film=film: self.open_fiche(film))
            self.grid_films.add_widget(img)

    
    def go_back(self, instance):
        self.manager.current = "menu"

    def open_fiche(self, film):
        fiche_screen = self.manager.get_screen("fiche_film")
        fiche_screen.afficher_fiche(film, previous_screen="all_films")
        self.manager.current = "fiche_film"

class FicheFilmScreen(BaseScreen4):
    def goto_filmographie(self, artiste_nom):
        if self.manager.has_screen("category_grid"):
            self.manager.remove_widget(self.manager.get_screen("category_grid"))
        all_films = self.manager.get_screen("all_films").load_films_from_folder()
        filtered = [f for f in all_films if f.get("artiste_nom", "").strip().lower() == artiste_nom.lower()]
        grid_screen = CategoryGridScreen(filtered, name="category_grid")
        if not self.manager.has_screen("category_grid"):
            self.manager.add_widget(grid_screen)
        self.manager.current = "category_grid"


    def open_categorie(self, keyword):
        all_films = self.manager.get_screen("all_films").load_films_from_folder()
        filtered = [f for f in all_films if keyword.lower() in f.get("categories", "").lower()]
        if self.manager.has_screen("category_grid"):
            self.manager.remove_widget(self.manager.get_screen("category_grid"))
        screen = CategoryGridScreen(filtered, name="category_grid", previous_screen="fiche_film")
        self.manager.add_widget(screen)
        self.manager.current = "category_grid"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        from kivy.uix.anchorlayout import AnchorLayout
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.retour)
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(anchor)
        self.scroll = ScrollView()
        self.content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.content.bind(minimum_height=self.content.setter('height'))
        self.scroll.add_widget(self.content)

        from kivy.uix.anchorlayout import AnchorLayout
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.retour)
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(self.scroll)

        self.add_widget(self.layout)

    def retour(self, instance):
        self.manager.current = "menu"

    
    def afficher_fiche(self, film, previous_screen="all_films"):
        from kivy.uix.anchorlayout import AnchorLayout
        self.content.clear_widgets()
        self.previous_screen = previous_screen

        def add_label(text, font_size=20, bold=False, align='left', spacing=10):
            halign = 'center' if align == 'center' else 'left'
            label = Label(
                text=text,
                font_size=font_size,
                halign=halign,
                valign='top',
                size_hint_y=None,
                bold=bold,
                text_size=(Window.width - 80, None),
                padding=(0, spacing)
            )
            label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1] + spacing))
            self.content.add_widget(label)

        titre = film.get("titre", "")
        titre_original = film.get("titre_original", "")
        realisateur = film.get("realisateur", "")
        annee = film.get("annee", "")
        acteurs = film.get("acteurs", "")
        duree = film.get("duree", "")
        resume = film.get("resume", "")
        categories = film.get("categories", "")

        # Bloc titre
        add_label(titre, font_size=30, bold=True, align='center', spacing=1)
        if titre_original and titre_original != titre:
            add_label(titre_original, font_size=18, align='center', spacing=1)

        self.content.add_widget(Label(size_hint_y=None, height=20))  # gros espacement entre blocs

        # Bloc infos
        
        add_label(f"Réalisé par {realisateur}", font_size=20, spacing=2)
        add_label(f"Sorti en {annee}", font_size=20, spacing=2)
        add_label(f"Avec {acteurs}", font_size=20, spacing=2)
        add_label(f"Durée : {duree}", font_size=20, spacing=2)

        self.content.add_widget(Label(size_hint_y=None, height=20))  # gros espacement entre blocs

        # Bloc résumé
        add_label(resume, font_size=18, align='left')

        self.content.add_widget(Label(size_hint_y=None, height=20))  # gros espacement entre blocs

        # Bloc filmographie
        artiste_nom = film.get("artiste_nom", "").strip()
        if artiste_nom:
            btn = Button(text="Filmographie", size_hint_y=None, height=40)
            btn.bind(on_release=lambda instance: self.goto_filmographie(artiste_nom))
            self.content.add_widget(btn)

        # Bloc catégories
        for cat in categories.split(','):
            cat = cat.strip()
            if cat:
                btn = Button(text=f"Catégorie : {cat}", size_hint_y=None, height=40)
                btn.bind(on_release=lambda instance, keyword=cat: self.open_categorie(keyword))
                self.content.add_widget(btn)


class CategoryGridScreen(BaseScreen3):
    def open_fiche(self, film):
        fiche_screen = self.manager.get_screen("fiche_film")
        fiche_screen.afficher_fiche(film, previous_screen=self.name)
        self.manager.current = "fiche_film"

    def __init__(self, films, previous_screen="categorie_choix", titre="", **kwargs):
        super().__init__(**kwargs)
        self.previous_screen = previous_screen

        layout = BoxLayout(orientation='vertical')

        from kivy.uix.anchorlayout import AnchorLayout
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.go_back)
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        layout.add_widget(anchor)

        # Titre
        self.titre_label = Label(
            text=titre,
            font_size=30,
            bold=True,
            halign='center',
            valign='middle',
            size_hint=(1, None),
            height=60,
            color=(1, 1, 1, 1)
        )
        self.titre_label.bind(size=lambda lbl, val: setattr(lbl, 'text_size', val))
        layout.add_widget(self.titre_label)

        # Grille
        scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        scroll.add_widget(self.grid)
        layout.add_widget(scroll)

        self.add_widget(layout)

        for film in films:
            affiche_path = os.path.join(film["folder_path"], "affiche.jpg")
            if os.path.isfile(affiche_path):
                img = ClickableImage(source=affiche_path, size_hint_y=None, height=200, allow_stretch=True, keep_ratio=True)
                img.bind(on_release=lambda instance, film=film: self.open_fiche(film))
                self.grid.add_widget(img)

    def go_back(self, instance):
        self.manager.current = self.previous_screen

    def next_film(self):
        self.index += 1
        self.show_film()

    def previous_film(self):
        self.index -= 1
        self.show_film()



class CategorieChoixScreen(BaseScreen2):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        from kivy.uix.anchorlayout import AnchorLayout
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        layout.add_widget(anchor)

        btn_artistes = Button(text="ARTISTES", size_hint=(1, 0.2))
        btn_artistes.background_normal = ''  # désactive l’image de fond par défaut
        btn_artistes.background_color = (1, 1, 1, 0.5)
        btn_artistes.font_name = 'assets/titres.ttf'
        btn_artistes.font_size = 35  # taille de police, par exemple 24 pixels
        btn_artistes.color = (0, 0, 0, 1)
        btn_artistes.bind(on_release=self.goto_artistes)
        layout.add_widget(btn_artistes)

        btn_annees = Button(text="ANNÉES", size_hint=(1, 0.2))
        btn_annees.background_normal = ''  # désactive l’image de fond par défaut
        btn_annees.background_color = (1, 1, 1, 0.5)
        btn_annees.font_name = 'assets/titres.ttf'
        btn_annees.font_size = 35  # taille de police, par exemple 24 pixels
        btn_annees.color = (0, 0, 0, 1)
        btn_annees.bind(on_release=self.ouvrir_ecran_menu_annees)
        layout.add_widget(btn_annees)

        btn_autres = Button(text="AUTRES", size_hint=(1, 0.2))
        btn_autres.background_normal = ''  # désactive l’image de fond par défaut
        btn_autres.background_color = (1, 1, 1, 0.5)
        btn_autres.font_name = 'assets/titres.ttf'
        btn_autres.font_size = 35  # taille de police, par exemple 24 pixels
        btn_autres.color = (0, 0, 0, 1)
        btn_autres.bind(on_release=self.goto_autres)
        layout.add_widget(btn_autres)

        self.add_widget(layout)

    def goto_artistes(self, instance):
        art_screen = self.manager.get_screen("categories_artistes")
        art_screen.refresh_artistes()
        self.manager.current = "categories_artistes"

    def goto_autres(self, instance):
        cat_screen = self.manager.get_screen("categories")
        cat_screen.refresh_categories()
        self.manager.current = "categories"

    def goto_annees(self, instance):
        films = charger_films()
        self.manager.get_screen('films_par_annees').charger_donnees(films)
        self.manager.current = 'films_par_annees'

    def ouvrir_ecran_annees(self, instance):
        films = charger_films_par_annees()
        ecran = self.manager.get_screen("annees")
        ecran.charger_films(films)
        self.manager.current = "annees"

    def ouvrir_ecran_menu_annees(self, instance):
        ecran = self.manager.get_screen("menu_annees")
        ecran.refresh_annees()
        self.manager.current = "menu_annees"




class ArtistesScreen(BaseScreen3):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.go_back)
        from kivy.uix.anchorlayout import AnchorLayout
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(anchor)

        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=2, spacing=[10, 30], size_hint_y=None, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

        self.add_widget(self.layout)

    def go_back(self, instance):
        self.manager.current = "categorie_choix"

    def refresh_artistes(self):
        self.grid.clear_widgets()
        all_films = self.manager.get_screen("all_films").load_films_from_folder()
        artiste_map = {}
        for film in all_films:
            artiste_entier = film.get("artiste_entier", "").strip()
            artiste_nom = film.get("artiste_nom", "").strip()
            if artiste_entier and artiste_nom:
                artiste_map.setdefault((artiste_nom, artiste_entier), []).append(film)

        import random
        for (nom, entier), films in sorted(artiste_map.items()):
            first = random.choice(films)
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=250, padding=5)
            label = Label(text=entier, size_hint_y=None, height=40, halign='center', valign='middle')
            label.bind(size=lambda lbl, val: setattr(lbl, 'text_size', val))
            img_path = os.path.join(first["folder_path"], "affiche.jpg")
            if os.path.isfile(img_path):
                img = ClickableImage(source=img_path, size_hint_y=None, height=200)
                img.bind(on_release=lambda instance, films=films: self.show_films(films))
                box.add_widget(label)
                box.add_widget(img)
                self.grid.add_widget(box)

    def show_films(self, films):
        if self.manager.has_screen("category_grid"):
            self.manager.remove_widget(self.manager.get_screen("category_grid"))
        grid_screen = CategoryGridScreen(films, name="category_grid")
        if not self.manager.has_screen("category_grid"):
            self.manager.add_widget(grid_screen)
        self.manager.current = "category_grid"


class VideoclubApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name="intro"))
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(AllFilmsScreen(name="all_films"))
        sm.add_widget(FicheFilmScreen(name="fiche_film"))
        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(RandomFilmScreen(name="random_film"))
        sm.add_widget(CategoriesScreen(name="categories"))
        sm.add_widget(CategorieChoixScreen(name="categorie_choix"))
        sm.add_widget(ArtistesScreen(name="categories_artistes"))
        sm.add_widget(FilmsParAnneeScreen(name="films_par_annees"))
        sm.add_widget(MenuAnnees(name="menu_annees"))
        return sm


class SearchScreen(BaseScreen3):
    def open_fiche(self, film):
        fiche_screen = self.manager.get_screen("fiche_film")
        fiche_screen.afficher_fiche(film)
        self.manager.current = "fiche_film"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        from kivy.uix.anchorlayout import AnchorLayout
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.retour)
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(anchor)

        self.search_input = TextInput(hint_text="Rechercher un film...", multiline=False, size_hint=(1, 0.1))
        self.search_button = Button(text="Chercher", size_hint=(1, 0.1))
        self.search_button.bind(on_release=self.launch_search)

        self.result_scroll = ScrollView(size_hint=(1, 0.8))
        self.result_grid = GridLayout(cols=3, spacing=10, size_hint_y=None)
        self.result_grid.bind(minimum_height=self.result_grid.setter('height'))
        self.no_result_label = Label(text="", size_hint_y=None, height=30)
        self.result_scroll.add_widget(self.result_grid)

        self.layout.add_widget(self.search_input)
        self.layout.add_widget(self.search_button)
        self.layout.add_widget(self.result_scroll)
        self.layout.add_widget(self.no_result_label)

        self.add_widget(self.layout)

    def retour(self, instance):
        self.manager.current = "menu"

    def launch_search(self, instance):
        query = self.search_input.text.strip().lower()
        self.result_grid.clear_widgets()
        self.search_input.text = ""
        self.no_result_label.text = ""
        all_films = self.manager.get_screen("all_films").load_films_from_folder()
        results_found = False

        for film in all_films:
            if any(query in str(film.get(field, '')).lower() for field in ["titre", "titre_original", "realisateur", "acteurs", "resume", "categories"]):
                affiche_path = os.path.join(film["folder_path"], "affiche.jpg")
                if os.path.isfile(affiche_path):
                    img = ClickableImage(source=affiche_path, size_hint_y=None, height=200, allow_stretch=True, keep_ratio=True)
                    img.bind(on_release=lambda instance, film=film: self.open_fiche(film))
                    self.result_grid.add_widget(img)
                    results_found = True

        if not results_found:
            self.no_result_label.text = "Aucun résultat trouvé."


class CategoriesScreen(BaseScreen2):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.go_back)
        from kivy.uix.anchorlayout import AnchorLayout
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(anchor)

        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=2, spacing=[10, 30], size_hint_y=None, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

        self.add_widget(self.layout)

    def go_back(self, instance):
        self.manager.current = "categorie_choix"

    def refresh_categories(self):
        self.grid.clear_widgets()
        all_films = self.manager.get_screen("all_films").load_films_from_folder()
        cat_map = {}
        for film in all_films:
            cats = film.get("categories", "").split(',')
            for cat in cats:
                cat = cat.strip()
                if cat:
                    cat_map.setdefault(cat, []).append(film)

        import random
        for cat, films in sorted(cat_map.items()):
            first = random.choice(films)
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=250, padding=5)
            label = Label(text=cat, size_hint_y=None, height=40, halign='center', valign='middle')
            label.bind(size=lambda lbl, val: setattr(lbl, 'text_size', val))
            img_path = os.path.join(first["folder_path"], "affiche.jpg")
            if os.path.isfile(img_path):
                img = ClickableImage(source=img_path, size_hint_y=None, height=200)
                img.bind(on_release=lambda instance, films=films: self.show_films(films))
                box.add_widget(label)
                box.add_widget(img)
                self.grid.add_widget(box)

    def show_films(self, films):
        if self.manager.has_screen("category_grid"):
            self.manager.remove_widget(self.manager.get_screen("category_grid"))
        grid_screen = CategoryGridScreen(films, name="category_grid")
        if not self.manager.has_screen("category_grid"):
            self.manager.add_widget(grid_screen)
        self.manager.current = "category_grid"


from kivy.uix.behaviors import DragBehavior

class SwipeImage(DragBehavior, ClickableImage):
    parent_screen = None
    parent_screen = None
    def reset_and_reload(self):
        from kivy.animation import Animation
        self.x = 0
        Animation(x=0, duration=0).start(self)
        self.parent.parent.show_random_film()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drag_distance = 20
        self.drag_timeout = 100
        self._touch_start_x = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._touch_start_x = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self._touch_start_x and abs(touch.x - self._touch_start_x) > 100:
            direction = 1 if touch.x > self._touch_start_x else -1
            from kivy.animation import Animation
            anim = Animation(x=self.x + direction * 600, duration=0.2)

            parent_screen = self.parent.parent.parent  # bien remonter jusqu'à RandomFilmScreen
            if parent_screen and hasattr(parent_screen, 'next_film') and hasattr(parent_screen, 'previous_film'):
                if direction == 1:
                    anim.bind(on_complete=lambda *a: parent_screen.previous_film())
                else:
                    anim.bind(on_complete=lambda *a: parent_screen.next_film())
            else:
                anim.bind(on_complete=lambda *a: self.reset_and_reload())

            anim.start(self)
        return super().on_touch_up(touch)

class RandomFilmScreen(BaseScreen4):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.films = []
        self.current_index = -1
        self.current_film = None

        container = RelativeLayout(size_hint=(1, 1))

        self.img = SwipeImage(size_hint=(None, None), width=400, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.img.allow_stretch = True
        self.img.keep_ratio = True
        container.add_widget(self.img)

        # Bind texture change to adjust height maintaining aspect ratio
        def adjust_img_height(instance, value):
            if instance.texture:
                tex_w, tex_h = instance.texture.size
                instance.height = instance.width * tex_h / tex_w
        self.img.bind(texture=adjust_img_height)

        self.img.bind(on_release=self.open_fiche)

        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''  # désactive l’image de fond par défaut
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35  # taille de police, par exemple 24 pixels
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=lambda inst: setattr(self.manager, 'current', 'menu'))
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)

        self.layout.add_widget(anchor)
        self.layout.add_widget(container)
        self.add_widget(self.layout)

    def load_films(self):
        self.films = self.manager.get_screen("all_films").load_films_from_folder()
        self.current_index = -1

    def show_film_by_index(self, index):
        if index < 0 or index >= len(self.films):
            return
        self.current_index = index
        film = self.films[index]
        self.current_film = film
        affiche_path = os.path.join(film["folder_path"], "affiche.jpg")
        self.img.source = affiche_path if os.path.isfile(affiche_path) else ""

    def show_random_film(self, *args):
        self.load_films()
        if not self.films:
            # Pas de self.label, donc juste vide l'image
            self.img.source = ""
            self.current_film = None
            self.current_index = -1
            return
        index = random.randint(0, len(self.films) -1)
        self.show_film_by_index(index)

    def next_film(self):
        if self.current_index < len(self.films) -1:
            self.show_film_by_index(self.current_index + 1)
        else:
            self.show_random_film()

    def previous_film(self):
        if self.current_index > 0:
            self.show_film_by_index(self.current_index - 1)

    def open_fiche(self, instance):
        if self.current_film:
            fiche_screen = self.manager.get_screen("fiche_film")
            fiche_screen.afficher_fiche(self.current_film)
            self.manager.current = "fiche_film"

class AnneesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        label = Label(text="Choisissez une année", font_size=24, size_hint=(1, 0.1))
        layout.add_widget(label)

        scroll = ScrollView(size_hint=(1, 0.9))
        grid = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=10)
        grid.bind(minimum_height=grid.setter('height'))

        # Tu peux personnaliser cette liste d'années ou la générer dynamiquement
        annees = [str(annee) for annee in range(1980, 2026)]

        for annee in annees:
            btn = Button(text=annee, size_hint_y=None, height=50)
            btn.bind(on_release=self.on_annee_select)
            grid.add_widget(btn)

        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def on_annee_select(self, instance):
        annee = instance.text
        print(f"Année sélectionnée : {annee}")
        # Rediriger vers un écran affichant les films de cette année
        # Tu peux par exemple faire :
        # self.manager.get_screen('films_par_annees').set_annee(annee)
        # self.manager.current = 'films_par_annees'

class FilmsParAnneeScreen(BaseScreen3):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        # Bouton retour
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.go_back)

        from kivy.uix.anchorlayout import AnchorLayout
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(anchor)

        self.titre_label = Label(
            text="",
            font_size=30,
            bold=True,
            halign='center',
            valign='middle',
            size_hint=(1, None),
            height=60,
            color=(1, 1, 1, 1)
        )
        self.titre_label.bind(size=lambda lbl, val: setattr(lbl, 'text_size', val))
        self.layout.add_widget(self.titre_label)
# Test
        self.titre_label.text = "Test"

        # ScrollView + Grille
        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=2, spacing=[10, 30], size_hint_y=None, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

        self.add_widget(self.layout)

        # Données
        self.annees = []
        self.index_annee = 0
        self._start_touch_x = None

    def go_back(self, instance):
        self.manager.current = "menu_annees"

    def charger_films_par_annees(self, annee):
        self.grid.clear_widgets()
        all_films = self.manager.get_screen("all_films").load_films_from_folder()

        # Construction de la liste des années
        self.annees = sorted(set(f.get("annee", "").strip() for f in all_films if f.get("annee", "").strip()))
        if annee in self.annees:
            self.index_annee = self.annees.index(annee)
        else:
            self.index_annee = 0

        annee_courante = self.annees[self.index_annee]
        self.titre_label.text = annee_courante
        films_annee = [f for f in all_films if f.get("annee", "").strip() == annee_courante]

        for film in films_annee:
            img_path = os.path.join(film["folder_path"], "affiche.jpg")
            if os.path.isfile(img_path):
                img = ClickableImage(
                    source=img_path,
                    size_hint_y=None,
                    height=250,
                    allow_stretch=True,
                    keep_ratio=True
                )
                img.bind(on_release=lambda instance, film=film: self.ouvrir_fiche(film))

                box = BoxLayout(
                    orientation='vertical',
                    size_hint_y=None,
                    height=250,
                    padding=5
                )
                box.add_widget(img)
                self.grid.add_widget(box)


    def ouvrir_fiche(self, film):
        self.manager.get_screen("fiche_film").afficher_fiche(film)
        self.manager.current = "fiche_film"



    # --- Swipe ---
    def on_touch_down(self, touch):
        self._start_touch_x = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self._start_touch_x is None:
            return super().on_touch_up(touch)
        delta = touch.x - self._start_touch_x
        if abs(delta) > 100:
            if delta > 0:
                self.annee_precedente()
            else:
                self.annee_suivante()
        return super().on_touch_up(touch)

    def annee_precedente(self):
        if self.index_annee > 0:
            self.index_annee -= 1
            self.charger_films_par_annees(self.annees[self.index_annee])

    def annee_suivante(self):
        if self.index_annee < len(self.annees) - 1:
            self.index_annee += 1
            self.charger_films_par_annees(self.annees[self.index_annee])



class MenuAnnees(BaseScreen3):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        # Bouton retour
        btn_back = Button(text="<", size_hint=(None, None), size=(50, 50))
        btn_back.background_normal = ''
        btn_back.background_color = (1, 1, 1, 0.5)
        btn_back.font_name = 'assets/titres.ttf'
        btn_back.font_size = 35
        btn_back.color = (0, 0, 0, 1)
        btn_back.bind(on_release=self.go_back)

        from kivy.uix.anchorlayout import AnchorLayout
        anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, None), height=60)
        anchor.add_widget(btn_back)
        self.layout.add_widget(anchor)

        # ScrollView + Grille
        self.scroll = ScrollView(size_hint=(1, 0.9))
        self.grid = GridLayout(cols=2, spacing=[10, 30], size_hint_y=None, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

        self.add_widget(self.layout)

    def go_back(self, instance):
        self.manager.current = "categorie_choix"

    def refresh_annees(self):
        self.grid.clear_widgets()

        # Chargement des films
        all_films = self.manager.get_screen("all_films").load_films_from_folder()

        # Création du dictionnaire des années -> films
        annees_map = {}
        for film in all_films:
            annee = film.get("annee", "").strip()
            if annee:
                annees_map.setdefault(annee, []).append(film)

        import random
        for annee, films in sorted(annees_map.items()):
            first = random.choice(films)

            # Affichage identique à ArtistesScreen
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=250, padding=5)

            label = Label(text=annee, size_hint_y=None, height=40, halign='center', valign='middle')
            label.bind(size=lambda lbl, val: setattr(lbl, 'text_size', val))

            img_path = os.path.join(first["folder_path"], "affiche.jpg")
            if os.path.isfile(img_path):
                img = ClickableImage(source=img_path, size_hint_y=None, height=200)
                img.bind(on_release=lambda instance, annee=annee: self.ouvrir_films_par_annees(annee))

                box.add_widget(label)
                box.add_widget(img)
                self.grid.add_widget(box)

    def ouvrir_films_par_annees(self, annee):
        ecran = self.manager.get_screen("films_par_annees")
        ecran.charger_films_par_annees(annee)
        self.manager.current = "films_par_annees"




if __name__ == "__main__":
    VideoclubApp().run()
