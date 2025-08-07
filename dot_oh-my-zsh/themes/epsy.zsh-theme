ARROW_SUCCESS_COLOR='240'
ARROW_FAILURE_COLOR='204'
PATH_COLOR='110'
GIT_COLOR='240'
SEPARATOR='>'
DIRTY_COLOR='138'
CLEAN_COLOR='240'

# If the branch is numbered (e.g. "1-my_branch", "13-feature3"), only show the number
git_prompt_info() {
    local ref
	GIT_ICON_COLOR=$CLEAN_COLOR
    if [[ "$(git_current_branch)" = 'HEAD' ]]; then
        ref=$(git rev-parse --short HEAD)
    else
        ref=$(git_current_branch)
        if [[ "$ref" =~ ^([0-9]+)- ]]; then
            ref="%{\e[3m%}${match[1]}"
        fi
    fi
    if [[ -n $(git status --porcelain 2>/dev/null) ]]; then
		GIT_ICON_COLOR=$DIRTY_COLOR
    fi
    if [[ $ref ]]; then
		ref="$FG[$GIT_ICON_COLOR]%{$reset_color%} $FG[$GIT_COLOR]${ref}%{$reset_color%}"
    fi
    echo "${ref}"
}


PROMPT='$FG[$PATH_COLOR]%c %(?.$FG[$ARROW_SUCCESS_COLOR].$FG[$ARROW_FAILURE_COLOR])$SEPARATOR%{$reset_color%} '
RPROMPT='$(git_prompt_info)'
