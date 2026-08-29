"""
REST API Chat & Conversation Endpoints.
"""

from flask import Blueprint, request, jsonify, session
from auth.rbac import login_required, get_current_user
from chatbot.response_engine import response_engine
from repositories.conversation_repository import conversation_repository
from repositories.message_repository import message_repository
from core.exceptions import ChatFlowException, NotFoundError

api_chat_bp = Blueprint("api_chat", __name__, url_prefix="/api")

@api_chat_bp.route("/chat", methods=["POST"])
@login_required
def chat():
    user = get_current_user()
    data = request.get_json() or {}
    conv_id = data.get("conversation_id")
    message_text = data.get("message", "").strip()

    if not message_text:
        return jsonify({"error": "Message cannot be empty"}), 422

    if not conv_id:
        conv = conversation_repository.create_conversation(user["id"], "New Chat")
        conv_id = conv["id"]

    try:
        res = response_engine.process_message(conv_id, message_text, user["id"])
        return jsonify({"status": "success", "conversation_id": conv_id, "result": res})
    except ChatFlowException as e:
        return jsonify(e.to_dict()), e.status_code

@api_chat_bp.route("/conversations", methods=["GET", "POST"])
@login_required
def conversations():
    user = get_current_user()
    if request.method == "POST":
        data = request.get_json() or {}
        title = data.get("title", "New Conversation")
        conv = conversation_repository.create_conversation(user["id"], title)
        return jsonify({"status": "success", "conversation": conv})

    user_convs = conversation_repository.get_user_conversations(user["id"])
    return jsonify({"status": "success", "conversations": user_convs})

@api_chat_bp.route("/conversations/<conv_id>", methods=["GET", "DELETE"])
@login_required
def conversation_detail(conv_id):
    user = get_current_user()
    conv = conversation_repository.find_by_id(conv_id)
    if not conv:
        raise NotFoundError("Conversation not found")

    if request.method == "DELETE":
        conversation_repository.delete(conv_id)
        return jsonify({"status": "success", "message": "Conversation deleted"})

    messages = message_repository.get_conversation_messages(conv_id)
    return jsonify({"status": "success", "conversation": conv, "messages": messages})
