import '@/styles/globals.css'
import { Inter as FontSans } from 'next/font/google'
import { ThemeProvider } from '@/components/theme-provider'

import { cn } from '@/lib/utils'
import Header from '@/components/header'

const fontSans = FontSans({
	subsets: ['latin'],
	variable: '--font-sans',
})

export const metadata = {
	title: 'Qwikz',
	description:
		'Simplify assessment and enhance learning with Qwikz. Create or take quizzes in no time.',
	icons: {
		icon: '/lightning.png',
	},
}

export default function RootLayout({ children }) {
	return (
		<html lang='en'>
			<body
				className={cn(
					'flex flex-col min-h-screen font-sans antialiased',
					fontSans.variable,
				)}
			>
				<ThemeProvider
					attribute='class'
					defaultTheme='system'
					enableSystem
					disableTransitionOnChange
				>
					<div className='absolute inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:16px_16px] dark:bg-[radial-gradient(#ffffff33_1px,#00091d_1px)] dark:bg-[size:20px_20px]'>
						<div className='absolute bottom-auto left-auto right-0 top-0 h-[500px] w-[500px] -translate-x-[30%] translate-y-[20%] rounded-full bg-[rgba(173,109,244,0.5)] opacity-50 blur-[80px]'></div>
					</div>
					<Header />
					{children}
				</ThemeProvider>
			</body>
		</html>
	)
}
