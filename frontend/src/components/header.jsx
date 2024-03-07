import Link from 'next/link'
import Image from 'next/image'
import { Montserrat } from 'next/font/google'
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import { GitHubLogoIcon } from '@radix-ui/react-icons'
import { ModeToggle } from '@/components/ui/mode-toggle'

const fontMontserrat = Montserrat({
	weights: [300, 400, 700],
	subsets: ['latin'],
})

export default function Header() {
	return (
		<header className='sticky top-0 z-50 w-full border-b border-border/80 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60'>
			<div className='container flex h-14 max-w-screen-2xl items-center justify-between'>
				<Link href='/' className='flex items-center space-x-1'>
					<Image
						src={'/lightning.png'}
						width={32}
						height={32}
						alt='qwikz-logo'
					/>
					<span className={cn('font-bold text-2xl', fontMontserrat.className)}>
						Qwikz
					</span>
				</Link>
				<nav className='flex items-center'>
					<Button asChild variant='ghost' size='icon'>
						<Link
							href={'https://github.com/chow-chow/Qwikz'}
							target='_blank'
							rel='noreferrer'
						>
							<GitHubLogoIcon className='h-4 w-4' />
							<span className='sr-only'>GitHub</span>
						</Link>
					</Button>
					<ModeToggle />
					<Button asChild variant='ghost'>
						<Link href={'/login'}>
							<span>Login</span>
						</Link>
					</Button>
				</nav>
			</div>
		</header>
	)
}
