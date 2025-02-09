import type { Config } from 'tailwindcss';
import daisyui from 'daisyui';
import plugin from '@tailwindcss/typography'

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {}
	},

	plugins: [daisyui, plugin],

	daisyui: {
		themes: ['light', 'dark', 'autumn', 'cmyk']
	}
} satisfies Config;
