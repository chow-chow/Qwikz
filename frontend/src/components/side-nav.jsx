import { Button } from '@/components/ui/button'
import { HomeIcon, PlusIcon, ExitIcon } from '@radix-ui/react-icons'
import Link from 'next/link'

// TODO: Add or remove things depending on the user's role
export default function SideNav() {
	return (
		<aside className='space-y-1 flex flex-col col-start-1 col-end-2 py-5 px-1 sticky left-0 z-40 border-r border-border/80 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60'>
			<Button asChild variant='ghost' className='md:justify-start'>
				<Link href={'#'}>
					<HomeIcon className='h-6 w-6 md:mr-2 md:h-5 md:w-5' />
					<span className='hidden md:block'>Home</span>
				</Link>
			</Button>
			<Button asChild variant='ghost' className='md:justify-start'>
				<Link href={'#'}>
					<PlusIcon className='h-6 w-6 md:mr-2 md:h5 md:w-5' />
					<span className='hidden md:block'>Create Group</span>
				</Link>
			</Button>
			<Button asChild variant='ghost' className='md:justify-start'>
				<Link href={'#'}>
					<ExitIcon className='h-6 w-6 md:mr-2 md:h-5 md:w-5' />
					<span className='hidden md:block'>Logout</span>
				</Link>
			</Button>
		</aside>
	)
}
