"""
Chat Interface View Blueprint.
"""

from flask import Blueprint, render_template, session, redirect, url_for
from auth.rbac import login_required, get_current_user
from repositories.conversation_repository import conversation_repository
from repositories.message_repository import message_repository

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
@chat_bp.route("/chat/<conversation_id>")
@login_required
def index(conversation_id=None):
    user = get_current_user()
    conversations = conversation_repository.get_user_conversations(user["id"])

    if not conversation_id and conversations:
        return redirect(url_for("chat.index", conversation_id=conversations[0]["id"]))
    elif not conversation_id:
        new_conv = conversation_repository.create_conversation(user["id"], "New Chat")
        return redirect(url_for("chat.index", conversation_id=new_conv["id"]))

    current_conv = conversation_repository.find_by_id(conversation_id)
    messages = message_repository.get_conversation_messages(conversation_id) if current_conv else []

    return render_template("chat.html", user=user, conversations=conversations, current_conv=current_conv, messages=messages)
