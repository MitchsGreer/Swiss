# =============================================================================
# Dockerfile for a python dev environment.
# =============================================================================
FROM python3.12

# -----------------------------------------------------------------------------
# Setup arguments and enironment variables.
# -----------------------------------------------------------------------------
ARG USERNAME=vscode \
    USER_UID=1280 \
    USER_GID=1280 \
    HOME_DIR=/home/vscode

# -----------------------------------------------------------------------------
# Add non-root user.
# -----------------------------------------------------------------------------
RUN  addgroup $USER_GID && \
    adduser -D -h $HOME_DIR -G $USER_GID -u $USER_UID $USERNAME && \
    addgroup -g $USER_GID $USERNAME
WORKDIR $HOME_DIR
USER $USERNAME
