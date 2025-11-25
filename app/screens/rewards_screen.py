"""
Pantalla de Recompensas - Reciclapp
Permite canjear eco-tokens por recompensas.
"""
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel




from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ObjectProperty

class RewardCard(MDCard):
    image_source = StringProperty('')
    title_text = StringProperty('')
    cost_text = StringProperty('')
    on_redeem = ObjectProperty(None)


class RewardsScreen(MDScreen):
    """
    Pantalla que muestra recompensas disponibles y permite canjearlas.
    """
    dialog = None
    
    def on_enter(self):
        """Al entrar, actualizar tokens y recompensas"""
        self.update_tokens_display()
        self.load_redeemed_history()
        
    def update_tokens_display(self):
        """Actualiza el contador de tokens"""
        app = MDApp.get_running_app()
        tokens = app.db.get_eco_tokens()
        self.ids.tokens_label.text = f"{tokens}"
        
    def load_redeemed_history(self):
        """Carga el historial de canjes"""
        app = MDApp.get_running_app()
        history = app.db.get_redeemed_rewards()
        
        self.ids.history_list.clear_widgets()
        
        from kivymd.uix.list import TwoLineListItem
        
        for item in history:
            list_item = TwoLineListItem(
                text=item['name'],
                secondary_text=f"Canjeado el {item['date_redeemed'][:10]}"
            )
            self.ids.history_list.add_widget(list_item)
            
    def confirm_redeem(self, reward_id, name, cost):
        """Muestra diálogo de confirmación"""
        app = MDApp.get_running_app()
        current_tokens = app.db.get_eco_tokens()
        
        if current_tokens < cost:
            self.show_error_dialog("No tienes suficientes EcoTokens.")
            return
            
        self.dialog = MDDialog(
            title="Canjear Recompensa",
            text=f"¿Deseas canjear '{name}' por {cost} tokens?",
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="CANJEAR",
                    on_release=lambda x: self.redeem(reward_id, name, cost)
                ),
            ],
        )
        self.dialog.open()
        
    def redeem(self, reward_id, name, cost):
        """Ejecuta el canje"""
        app = MDApp.get_running_app()
        success = app.db.redeem_reward(reward_id, name, cost)
        
        if success:
            self.close_dialog()
            self.update_tokens_display()
            self.load_redeemed_history()
            self.show_success_dialog(f"¡Disfruta tu {name}!")
        else:
            self.close_dialog()
            self.show_error_dialog("Error al procesar el canje.")
            
    def close_dialog(self, *args):
        """Cierra el diálogo"""
        if self.dialog:
            self.dialog.dismiss()
            
    def show_error_dialog(self, text):
        """Muestra error"""
        self.dialog = MDDialog(
            title="Error",
            text=text,
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)]
        )
        self.dialog.open()
        
    def show_success_dialog(self, text):
        """Muestra éxito"""
        self.dialog = MDDialog(
            title="¡Canje Exitoso!",
            text=text,
            buttons=[MDFlatButton(text="GENIAL", on_release=self.close_dialog)]
        )
        self.dialog.open()
            
    def volver_home(self):
        """Vuelve al inicio"""
        self.manager.current = 'home'

# Cargar el diseño KV al final para asegurar que las clases estén definidas
Builder.load_file('app/screens/rewards_screen.kv')
