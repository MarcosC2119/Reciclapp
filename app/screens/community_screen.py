"""
Pantalla de Comunidad - Reciclapp
"""
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from app.database import Database

# Cargar el diseño KV de esta pantalla
Builder.load_file('app/screens/community_screen.kv')


class PostItem(MDCard):
    """Widget para representar un post en el feed"""
    author_name = StringProperty()
    time_text = StringProperty()
    content_text = StringProperty()
    likes_count = StringProperty("0")
    comments_count = StringProperty("0")


class CommunityScreen(MDScreen):
    """Pantalla de comunidad para conectar con otros usuarios"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        
    def on_enter(self):
        """Se llama al entrar a la pantalla"""
        self.refresh_feed()
        
    def refresh_feed(self):
        """Recarga el feed de publicaciones"""
        # Limpiar feed actual
        feed_container = self.ids.feed_container
        feed_container.clear_widgets()
        
        # Obtener posts de la BD
        posts = self.db.get_community_posts()
        
        # Si no hay posts, mostrar mensaje o posts de ejemplo
        if not posts:
            self.add_example_posts()
            posts = self.db.get_community_posts()
            
        # Agregar posts al feed
        for post in posts:
            item = PostItem()
            item.author_name = post.get('author', 'Usuario')
            item.time_text = f"hace un momento • {post.get('location', 'Reciclapp')}"
            item.content_text = post.get('content', '')
            item.likes_count = str(post.get('likes', 0))
            item.comments_count = str(post.get('comments', 0))
            feed_container.add_widget(item)
            
    def add_example_posts(self):
        """Agrega posts de ejemplo si la BD está vacía"""
        self.db.add_community_post("Ana López", "¡Logré mi meta semanal! 25 botellas recicladas 🌿", "Polanco, CDMX")
        self.db.add_community_post("Carlos Mendoza", "Encontré un nuevo EcoPunto súper organizado. ¡Recomendado!", "Roma Norte, CDMX")

    def publicar_post(self):
        """Publica un nuevo post"""
        input_field = self.ids.post_input
        text = input_field.text.strip()
        
        if text:
            # Obtener usuario actual
            user = self.db.get_user()
            author = user.get('name', 'Ana Martínez')
            
            # Guardar en BD
            self.db.add_community_post(author, text, "Mi Ubicación")
            
            # Limpiar y recargar
            input_field.text = ""
            self.refresh_feed()

    def navegar_home(self):
        """Navega a la pantalla de inicio"""
        self.manager.current = 'home'

    def navegar_logros(self):
        """Navega a la pantalla de logros"""
        self.manager.current = 'achievements'

    def navegar_perfil(self):
        """Navega a la pantalla de perfil"""
        self.manager.current = 'profile'

    def escanear_qr(self):
        """Maneja la acción de escanear QR"""
        print("Escanear QR presionado")

