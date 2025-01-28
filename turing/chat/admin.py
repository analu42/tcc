from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    # Configurações para exibir colunas específicas na lista de mensagens
    list_display = ('id', 'sender', 'text_preview', 'timestamp')  
    list_filter = ('sender', 'timestamp')  # Permite filtrar por remetente e data
    search_fields = ('sender', 'text')  # Campo de busca
    ordering = ('-timestamp',)  # Ordena as mensagens pela data mais recente

    # Função personalizada para exibir um preview do texto
    def text_preview(self, obj):
        return obj.text[:50] + ("..." if len(obj.text) > 50 else "")
    text_preview.short_description = "Preview do Texto"

# Registrando o modelo e a configuração personalizada
admin.site.register(Message, MessageAdmin)
