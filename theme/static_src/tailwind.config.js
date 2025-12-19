/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#4B0082',
                    light: '#6B238E',
                    dark: '#2E0854',
                },
                secondary: {
                    DEFAULT: '#1E90FF',
                    light: '#4DA6FF',
                },
            },
        },
    },
    plugins: [],
}
