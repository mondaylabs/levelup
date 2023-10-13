import {css, StyleSheet} from 'aphrodite'
import React from 'react'
import cn from 'classnames'

export default function Button({
                                   text, onClick, loading=false, className, icon, disabled = false, type = 'button', ...rest
                               }) {
    return (
        <button
            onClick={onClick}
            type={type}
            disabled={disabled}
            className={cn('btn', className,)}
            {...rest}>

            {icon ? <i className={cn('icon', text ? css(styles.icon) : '', icon)}/> : null}
            {!loading ? text : <span className="loading loading-spinner"></span>}
        </button>
    )
}

const styles = StyleSheet.create({
    icon: {
        marginRight: '0.2rem',
    },
})
